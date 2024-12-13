import calendar
import os
import shutil
import uuid
from enum import Enum
from pathlib import Path
from typing import Dict

import yaml

from ...shared.DataGouvException import DataGouvException
from ...shared.ParquetFile import ParquetFile
from ...shared.types import AssetTypes
from ...use_cases.finance.submodule.finance.scripts.utils.Consts import DATA_FOLDER


def get_last_day(mois: str, annee: str) -> str:
    """
    Retourne le dernier jour du mois pour une année donnée.

    :param mois: Le mois (en chaîne, "01" pour janvier jusqu'à "12" pour décembre).
    :param annee: L'année (en chaîne, "YYYY").
    :return: Le dernier jour du mois en tant que chaîne.
    """
    try:
        mois_int = int(mois)
        annee_int = int(annee)

        if mois_int < 1 or mois_int > 12:
            raise ValueError("Le mois doit être compris entre '01' et '12'.")

        dernier_jour = calendar.monthrange(annee_int, mois_int)[1]
        return str(dernier_jour)
    except ValueError as e:
        return f"Erreur : {e}"


def load_yaml(config_path: str, base_path: str = None, **kwargs) -> dict:
    """
    Charge un fichier YAML et retourne son contenu.

    Args:
        config_path (str): Chemin relatif du fichier YAML à partir de base_path ou utils.py si non spécifié.
        base_path (str): Chemin de base pour résoudre le fichier YAML. Par défaut, le répertoire parent de `utils.py`.
        **kwargs: Options supplémentaires, comme `encoding`.

    Returns:
        dict: Contenu du fichier YAML sous forme de dictionnaire.
    """
    if base_path is None:
        base_path = Path(__file__).resolve().parent.parent  # data_gov racine
    else:
        base_path = Path(base_path).resolve()

    full_path = base_path / config_path

    try:
        with open(full_path, "r", encoding=kwargs.get("encoding", "utf-8")) as f:
            config_file = yaml.safe_load(f)
        return config_file
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Le fichier de configuration {full_path} est introuvable.") from e
    except yaml.YAMLError as e:
        raise ValueError(f"Erreur lors de la lecture du fichier YAML : {full_path}") from e


def get_params(asset_type: AssetTypes, source_name: str, params: str):
    try:
        config_file = load_yaml(config_path="finance/submodule/finance/conf/parameters.yaml")

        search = config_file["assets"][asset_type.value]["source"][source_name]
        return search.get(params)
    except Exception as e:
        raise DataGouvException(
            title="Get Function Name",
            description=f"Des erreurs ont été détectées lors de la recupération de la fonction pour l'asset {asset_type.value} et la source {source_name}.\nErreur détaillé: {str(e)}"
        )


def get_sources(asset_type: AssetTypes, file_type: str):
    try:
        config_file = load_yaml(config_path="finance/submodule/finance/conf/parameters.yaml")
        return [file for file, file_ in config_file['assets'][asset_type.value.upper()]['source'].items() if
                file_['filename_contains'].upper() == file_type.upper()]
    except Exception as e:
        raise DataGouvException(
            title="Get File Type Source ",
            description=f"Des erreurs ont été détectées lors de la recupération de la fonction pour l'asset {asset_type.value} et la source {file_type}.\nErreur détaillé: {str(e)}"
        )


def create_directory(file_asset, file_type):
    relative_tmp_path = DATA_FOLDER + '/raw'
    directory_path = f"{relative_tmp_path}/{file_asset}/{file_type}"
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def copy_to_directories(file_path: str, file_asset: AssetTypes, file_type: Enum):
    """
    Copie le fichier dans les répertoires appropriés en fonction de l'actif et du type de fichier.
    """
    path = get_params(file_asset, file_type.value.lower(), "path")
    final_directory = create_directory(file_asset.value, path)
    shutil.copy(file_path, final_directory)


def add_parquet_file(tmp_parquet_files_dict: Dict[uuid.UUID, ParquetFile], asset: AssetTypes, use_case: str,
                     file_name: str, file_source: str, parquet_file_path: str, classic_file_path: str | None):
    print(asset, use_case, file_name, file_source, parquet_file_path)
    session_id = uuid.uuid4()
    tmp_parquet_files_dict[session_id] = ParquetFile(asset, use_case, file_name, file_source, parquet_file_path,
                                                     classic_file_path)
    return session_id
