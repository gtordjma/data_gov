import asyncio
import copy
import datetime
from io import BytesIO
import os
from pathlib import Path
import tempfile
import time
from typing import Dict, List, Optional, Tuple

from fastapi import HTTPException, UploadFile

from submodules.data_gov.use_cases.finance.FinanceFileTypes import FinanceFileTypes

from .utils.gcp import download_file_from_tmp_bucket, generate_signed_url_and_download

from .DataGouvException import DataGouvException
from .types.AssetTypes import AssetTypes
from .types.FileStepStatus import FileStepStatus
from ..use_cases.finance.FinanceFile import FinanceFile
from ..use_cases.finance.ProcessFinanceFile import get_check_ref_messages, process_file
from ..use_cases.finance.Utils import add_parquet_file
from ..use_cases.finance.KpisFunctions import kpis_function_tab

from google.cloud import storage
from google.oauth2 import service_account

def local_file_to_uploadfile(file_path: str) -> UploadFile:
    # Read the file from the local path
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Open the file and read its contents
    with path.open("rb") as file:
        file_content = file.read()

    # Simulate the UploadFile object
    upload_file = UploadFile(
        filename=path.name,
        file=BytesIO(file_content),
    )

    return upload_file

async def process_file_wrapper(
    file_name: str,
    running_date: str,
    file_path: str,
    file_type_source: FinanceFileTypes,
    file_asset: AssetTypes,
    finance_file: 'FinanceFile',
    tmp_parquet_files_dict: Dict,
    version: str | None
) -> Dict:
    """
    Wrapper pour process_file qui gère les erreurs et retourne un dictionnaire formaté
    """
    try:
        local_parquet_file = await asyncio.to_thread(download_file_from_tmp_bucket, file_asset, "finance", file_type_source.value, running_date)
        check_ref_messages = await asyncio.to_thread(
                get_check_ref_messages,
                file_name,
                file_path,
                file_type_source,
                file_asset
            )
        if not local_parquet_file:
            kpis, parquet_file_path = await asyncio.to_thread(
                process_file,
                file_name,
                running_date,
                file_path,
                file_type_source,
                file_asset
            )

            finance_file.update_status("checkKpis", FileStepStatus.RUNNING)

            file_id = await asyncio.to_thread(
                add_parquet_file,
                tmp_parquet_files_dict,
                file_asset,
                "finance",
                file_name,
                file_type_source.value,
                parquet_file_path,
                file_path
            )
        else:
            kpis = kpis_function_tab[file_type_source](local_parquet_file) if file_type_source in kpis_function_tab else {"no_kpis_function": [[""],[""]]}
            finance_file.update_status("checkKpis", FileStepStatus.RUNNING)
            parquet_file_path = local_parquet_file
            file_id = None
        
        return {
            "success": True,
            "version": version,
            "file_type_source": f"{file_asset.value.lower()}_{file_type_source.value}",
            "status": copy.deepcopy(finance_file.status),
            "kpis": kpis,
            "file_id": str(file_id),
            "check_ref_messages": check_ref_messages
        }
        
    except DataGouvException as dge:
        finance_file.update_status("checkKpis", FileStepStatus.ERROR)
        return {
            "success": False,
            "file_type_source": f"{file_asset.value.lower()}_{file_type_source.value}",
            "status": copy.deepcopy(finance_file.status),
            "error": {
                "title": dge.title,
                "description": dge.description
            }
        }
    except Exception as e:
        finance_file.update_status("checkKpis", FileStepStatus.ERROR)
        print(f"Error type: {type(e)}")
        if isinstance(e, IndexError):
            print(f"IndexError occurred at {e.__traceback__.tb_frame.f_code.co_name}, line {e.__traceback__.tb_lineno}")
        
        return {
            "success": False,
            "file_type_source": f"{file_asset.value.lower()}_{file_type_source.value}",
            "status": copy.deepcopy(finance_file.status),
            "error": {
                "title": "Internal Error:",
                "description": str(e)
            }
        }

async def handle_pending_status(
    tmp_parquet_files_dict,
    template: Dict,
    entry: Dict,
    file_asset: AssetTypes,
    use_case: str
) -> None:
    """
    Gère le statut 'pending' avec traitement parallèle des fichiers.
    """
    total_start = time.time()
    
    template["status"].update({
        "loaded": FileStepStatus.FINISHED,
        "checkfile": FileStepStatus.FINISHED,
        "checkKpis": FileStepStatus.RUNNING
    })
    
    # Mesurer le temps de génération de l'URL signée
    url_start = time.time()
    signed_url, local_path = await asyncio.to_thread(
        generate_signed_url_and_download,
        entry["landing_url"],
        download_locally=True
    )
    print(f"URL generation and download took {time.time() - url_start:.2f} seconds")
    
    # Mesurer le temps de création du UploadFile
    upload_start = time.time()
    uploaded_file = await asyncio.to_thread(local_file_to_uploadfile, local_path)
    print(f"Upload file creation took {time.time() - upload_start:.2f} seconds")
    
    finance_file = FinanceFile(
        file=uploaded_file,
        file_asset=file_asset,
        file_type=template["file_type"],
        year=entry["date"]["year"],
        month=entry["date"]["month"],
        file_version=template["version"] if "version" in template else None
    )
    
    # Mesurer le temps de sauvegarde
    save_start = time.time()
    file_name, running_date, file_path = await finance_file.save_file_to_tmp_folder()
    print(f"File save took {time.time() - save_start:.2f} seconds")
    
    print("file_name, running_date, file_path", file_name, running_date, file_path)
    print(finance_file.sources)
    
    # Création et exécution parallèle des tâches
    process_start = time.time()
    tasks = [
        process_file_wrapper(
            file_name,
            running_date,
            file_path,
            file_type_source,
            file_asset,
            finance_file,
            tmp_parquet_files_dict,
            template["version"] if "version" in template else None
        )
        for file_type_source in finance_file.sources
    ]
    
    results = await asyncio.gather(*tasks)
    print(f"Parallel processing took {time.time() - process_start:.2f} seconds")
    
    template["finance_file_data"] = results
    print(f"Total pending status handling took {time.time() - total_start:.2f} seconds")

async def update_status_and_processing(
    tmp_parquet_files_dict,
    template: Dict,
    entry: Dict,
    asset: AssetTypes,
    use_case: str
) -> None:
    """
    Met à jour le statut et effectue le traitement selon le statut.
    """
    status_handlers = {
        "pending": handle_pending_status,
        "running": handle_running_status,
        "success": handle_success_status,
        "failed": handle_failed_status
    }
    
    handler = status_handlers.get(entry["status"])
    if handler:
        if entry["status"] == "pending":
            await handler(tmp_parquet_files_dict, template, entry, asset, use_case)
        else:
            handler(tmp_parquet_files_dict, template, entry, asset, use_case)

def update_error_info(template: Dict, entry: Dict) -> None:
    """
    Met à jour les informations d'erreur si présentes.
    """
    if (entry.get("cause") and entry.get("cause") != "") or \
       (entry.get("detailed_cause") and entry.get("detailed_cause") != ""):
        template["error"] = {
            "title": entry.get("cause"),
            "description": entry.get("detailed_cause")
        }

def update_basic_info(template: Dict, entry: Dict) -> None:
    """
    Met à jour les informations de base du template.
    """
    def format_reception_time(reception_time: Optional[datetime.datetime]) -> str:
        """
        Formate le temps de réception en chaîne de caractères.
        """
        if isinstance(reception_time, datetime.datetime):
            return reception_time.strftime("%Y-%m-%d %H:%M:%S")
        return ""
    template.update({
        "final_filename": entry.get("final_filename"),
        "url": entry.get("url"),
        "uploaded_by": "sftp" if "sftp" in entry.get("url", "") else "sdh portal",
        "landing_url": entry.get("landing_url"),
        "date": format_reception_time(entry.get("reception_time"))
    })

async def update_template_with_entry(
    tmp_parquet_files_dict,
    template: Dict,
    entry: Dict,
    asset: AssetTypes,
    use_case: str
) -> None:
    """
    Met à jour le template avec les informations de l'entrée.
    """
    update_basic_info(template, entry)
    update_error_info(template, entry)
    await update_status_and_processing(tmp_parquet_files_dict, template, entry, asset, use_case)

async def update_data_template(
    tmp_parquet_files_dict: Dict,
    data_template: List[Dict],
    process_data: List[Dict],
    year: int,
    month: int,
    asset: AssetTypes,
    use_case: str
) -> List[Dict]:
    # Création des tâches pour chaque mise à jour
    update_tasks = []
    
    for template_name, sources_list in data_template.items():
        for source in sources_list:
            for entry in process_data:
                if is_valid_entry(entry, source, year, month):
                    task = update_template_with_entry(
                        tmp_parquet_files_dict, source, entry, asset, use_case
                    )
                    update_tasks.append(task)
    
    # Exécution de toutes les mises à jour en parallèle
    await asyncio.gather(*update_tasks)
    
    return data_template


def is_valid_entry(entry: Dict, template: Dict, year: int, month: int) -> bool:
    """
    Vérifie si l'entrée est valide et correspond aux critères de mise à jour.
    """
    def is_valid_landing_url(url: Optional[str]) -> bool:
        """
        Vérifie si l'URL d'atterrissage est valide.
        """
        return url not in (None, 'None') and "None" not in str(url)

    if not is_valid_landing_url(entry.get("landing_url")):
        return False
    return (
        entry["file_type"] == template["source"] and
        entry.get("date", {}).get("year") == year and
        entry.get("date", {}).get("month") == month and
        ("version" not in template or template["version"] in entry.get("final_filename", ""))
        )

def handle_running_status(
    tmp_parquet_files_dict,
    template: Dict,
    entry: Dict,
    asset: AssetTypes,
    use_case: str
) -> None:
    """
    Gère le statut 'running'.
    """
    template["status"].update({
        "loaded": FileStepStatus.FINISHED,
        "checkfile": FileStepStatus.RUNNING
    })
def handle_success_status(
    tmp_parquet_files_dict,
    template: Dict,
    entry: Dict,
    asset: AssetTypes,
    use_case: str
) -> None:
    """
    Gère le statut 'success'.
    """
    template["status"].update({
        "loaded": FileStepStatus.FINISHED,
        "checkfile": FileStepStatus.FINISHED,
        "checkKpis": FileStepStatus.FINISHED,
        "processed": FileStepStatus.FINISHED
    })
def handle_failed_status(
    tmp_parquet_files_dict,
    template: Dict,
    entry: Dict,
    asset: AssetTypes,
    use_case: str
) -> None:
    """
    Gère le statut 'failed'.
    """
    template["status"].update({
        "loaded": FileStepStatus.FINISHED,
        "checkfile": FileStepStatus.ERROR
    })

def handle_error(template: Dict, error: Exception) -> None:
    """
    Gère les erreurs et met à jour le template en conséquence.
    """
    template["status"].update({
        "loaded": FileStepStatus.FINISHED,
        "checkfile": FileStepStatus.ERROR,
        "checkKpis": FileStepStatus.PENDING,
        "processed": FileStepStatus.PENDING
    })

    if isinstance(error, DataGouvException):
        template["error"] = {
            "title": error.title,
            "description": error.description
        }
    else:
        template["error"] = {
            "title": "Sync DB Data Error",
            "description": str(error)
        }
        
        
def clean_final_data(original_data):
    # On itère sur chaque asset dans original_data, par exemple "LGW"
    for asset, records in original_data.items():
        # records est une liste d'objets
        if not isinstance(records, list):
            continue  # si ce n'est pas une liste, on skip

        # Construction d'une map source -> objet pour chaque asset
        source_map = {}
        version_map = {}  # Map séparée pour les objets sans version
        
        for obj in records:
            if "source" in obj:
                source = obj["source"]
                version = obj.get("version")
                
                # Stockage dans la map appropriée
                if version is not None:
                    source_map[(source, version)] = obj
                else:
                    # Si pas de version, on stocke dans une map séparée
                    if source not in version_map:
                        version_map[source] = []
                    version_map[source].append(obj)

        # Parcours des objets de la liste
        for obj in records:
            if "finance_file_data" in obj:
                for elem in obj["finance_file_data"]:
                    target_source = elem.get("file_type_source")
                    target_version = elem.get("version")
                    
                    target_obj = None
                    
                    if target_source:
                        if target_version is not None:
                            # Cas avec version spécifiée
                            target_key = (target_source, target_version)
                            if target_key in source_map:
                                target_obj = source_map[target_key]
                        else:
                            # Cas sans version - on prend le premier objet correspondant sans version
                            if target_source in version_map and version_map[target_source]:
                                target_obj = version_map[target_source][0]

                        if target_obj:
                            # Mise à jour de l'élément cible
                            for key, value in elem.items():
                                if key not in ["file_type_source", "version"]:
                                    target_obj[key] = value

                            # Suppression de "finance_file_data" de l'objet cible si existant
                            if "finance_file_data" in target_obj:
                                del target_obj["finance_file_data"]

    return original_data