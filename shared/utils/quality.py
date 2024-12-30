import asyncio
from collections import defaultdict
from datetime import datetime
from functools import partial
import re
from .easy_env import easy_env


async def get_quality_data(use_case: str, asset: str, year: str, month: str):
    try:
        query = f"""
        SELECT *
        FROM `va-sdh-hq-staging.monitoring.sdh_file_status`
        WHERE use_case = '{use_case}'
              AND asset = '{asset}'
              AND file_name_sftp LIKE '%_{year}-{month}-%'
        """
        loop = asyncio.get_event_loop()
        query_job = await loop.run_in_executor(None, partial(easy_env.gcloud.BQ.query, query))
        results = await loop.run_in_executor(None, query_job.result)
        rows = [dict(row) for row in results]
        return rows
    except Exception as e:
        print(e)
        return []
    
async def get_quality_data_formatted_from_ingestion(use_case: str, asset: str, year: str, month: str):
    quality_data = await get_quality_data(use_case, asset, year, month)
    print("quality_data OG", quality_data)
    
    # Formatage des données
    for entry in quality_data:
        if entry["landing_url"] and entry["landing_url"] != "None":
            final_filename = entry["landing_url"].split("/")[-1]
            entry["final_filename"] = final_filename
            
            date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', final_filename)
            entry["date"] = {
                "year": date_match.group(1),
                "month": date_match.group(2),
                "day": date_match.group(3)
            } if date_match else None
        else:
            entry["final_filename"] = None
            entry["date"] = None

    # Patterns pour détecter les versions dans les noms de fichiers
    version_patterns = {
        'capex_forecast': r'FINANCE_CPXFORECAST_(B0|R[1-9])',
        'budget': r'FINANCE_BUDGET_(B0|R[1-9])'
    }
    
    grouped_by_type = defaultdict(list)
    grouped_by_version = defaultdict(list)
    
    # Groupement selon le type de fichier
    for entry in quality_data:
        file_type = entry["file_type"]
        
        # Vérification pour les deux types spéciaux
        is_special_type = False
        for type_key, pattern in version_patterns.items():
            if type_key in file_type.lower():
                match = re.search(pattern, entry["file_name_sftp"])
                if match:
                    version = match.group(1)
                    grouped_by_version[version].append(entry)
                    is_special_type = True
                    break
                    
        if not is_special_type:
            grouped_by_type[file_type].append(entry)
    
    result = []
    
    # Traitement des fichiers standards
    for entries in grouped_by_type.values():
        most_recent = max(entries, key=lambda x: (
            x["reception_time"] if isinstance(x["reception_time"], datetime)
            else datetime.strptime(x["reception_time"], '%Y-%m-%d %H:%M:%S')
        ))
        result.append(most_recent)
    
    # Traitement des fichiers avec versions
    for entries in grouped_by_version.values():
        most_recent = max(entries, key=lambda x: (
            x["reception_time"] if isinstance(x["reception_time"], datetime)
            else datetime.strptime(x["reception_time"], '%Y-%m-%d %H:%M:%S')
        ))
        result.append(most_recent)

    return result