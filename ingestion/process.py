from enum import Enum
import importlib
import re

from fastapi import UploadFile
import pandas as pd
import pandera as pa
from data_gov.ingestion.check_file import validate_asset, validate_filename_type
from data_gov.error import DataGouvException
from data_gov.ingestion.utils import copy_to_directories, load_yaml, split_name
from data_gov.types import AssetTypes
from data_gov.kpis import kpis_function_tab
from data_gov.finance.scripts.ProcessingFunction import processing_function

def get_special_function_name(file_type: Enum, asset_type: AssetTypes) -> None:
    try:
        print(f"Traitement du fichier contenant '{file_type.value}' pour l'actif '{asset_type.value}'.")
        config_file = load_yaml("parameters.yaml", encoding="utf-8")

        search = config_file["assets"][asset_type.value]["source"]

        for key in search.values():
            if key.get("filename_contains") == file_type.value:
                return key.get("loadfile_call")
    except Exception as e:
        raise DataGouvException(
            title="Get Function Name",
            description=f"Des erreurs ont été détectées lors de la recupération de la fonction pour l'asset {asset_type.value} et le type {file_type.value}.\nErreur détaillé: {str(e)}"
        )
        
def load_dataset(filepath: UploadFile | str, func_name: str, file_type: Enum, asset_type: AssetTypes) -> pd.DataFrame:
    try:
        print("load_dataset filepath", filepath)
        parts = func_name.split('_')
        first_dir = parts[0]  # ex: 'kap'

        sub_dirs = parts[1:-1]  
        sub_dir = '_'.join(sub_dirs)

        module_path = f'assets.{first_dir}.{sub_dir}.read'

        read_module = importlib.import_module(module_path)

        read_function = getattr(read_module, 'read')

        df = read_function(filepath)
        return df
    except Exception as e:
        raise DataGouvException(
            title="Load Dataset Error",
            description=f"Le fichier envoyé ne correspond pas pour l'asset {asset_type.value} et le type {file_type.value}.\nErreur détaillé: {str(e)}"
        )

def get_schema_module(file_asset: AssetTypes, file_type: str):
    schema_module_path = '.'.join(['assets', file_asset.value.lower(), file_type, 'schema'])

    try:
        schema_module = importlib.import_module(schema_module_path)
    except ModuleNotFoundError:
        raise Exception(f"Le schéma pour {'/'.join([file_asset.value.lower(), file_type])} n'a pas été trouvé.")

    return schema_module

def transform_dataframe_for_kap(df: pd.DataFrame, schema: pa.DataFrameSchema, funcname) -> tuple[pd.DataFrame, pa.DataFrameSchema]:
    if funcname[:3].lower() == "kap" and any(
        substring in funcname.lower() for substring in ("capex", "forecast", "budget", "ledger")
    ):
        kap_regex = r"\w{3}\s.*"
        add_to_col = "actual or estimate"

        df.columns = [
            col[:3] + add_to_col if re.match(kap_regex, col) else col
            for col in df.columns
        ]

        schema_columns = {}
        for col_name, column in schema.columns.items():
            transformed_col_name = col_name
            if re.match(kap_regex, col_name):
                transformed_col_name = col_name[:3] + add_to_col
            schema_columns[transformed_col_name] = column

        schema = pa.DataFrameSchema(
            columns=schema_columns,
            strict=schema.strict,
            coerce=schema.coerce,
        )

    return df, schema

def validate_dataframe_with_schema(df: pd.DataFrame, schema: pa.DataFrameSchema):
    try:
        schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as err:
        error_message = "The following columns are missing from your file:<br/>"
        for failure in err.failure_cases.itertuples():
            error_message += f"{failure.failure_case}, "
        raise DataGouvException(
            title="Validate Schema Error",
            description=error_message
        )

def validate_file_schema(filepath: str, file_asset: AssetTypes, file_type: str, func_name):
    df = load_dataset(filepath, func_name, file_type, file_asset)
    schema_module = get_schema_module(file_asset, file_type)
    schema: pa.DataFrameSchema | None = getattr(schema_module, 'schema', None)
    if schema is None:
        raise Exception(f"Aucun schéma trouvé dans le module '{schema_module.__name__}'.")

    df, schema = transform_dataframe_for_kap(df, schema, func_name)

    validate_dataframe_with_schema(df, schema)

def process_file(filename, running_date: str, filepath: str):
    """
    Processus complet de traitement d'un fichier valide.
    """
    file_type = validate_filename_type(filename)
    file_asset = validate_asset(filename)
    
    #if file_type and file_asset and "LGW_FINANCE" in filename:
    if file_type and file_asset:
        print("file_type, file_asset", file_type, file_asset)
        func_name = get_special_function_name(file_type, file_asset)

        # Valider le schéma
        validate_file_schema(filepath, file_asset, split_name(func_name)[1], func_name)
        
        # Copier le fichier dans les répertoires nécessaires
        print(filepath, file_asset, file_type)
        copy_to_directories(filepath, file_asset, file_type)
        
        # Exécuter la fonction de traitement
        file_source = f"finance_{file_type.value.lower()}"
        #relative_path = Path(__file__).parent / 'parameters.yaml'
        #relative_tmp_path = Path(__file__).parent / 'tmp'
        try:
            files = processing_function(file_asset.value, file_source, running_date)
        except Exception as e:
            #pprint(traceback.format_exception(type(e), e, e.__traceback__))
            raise DataGouvException(
                title="Processing Function Error",
                description=f"{str(e)}"
            )     

        if file_type.value in kpis_function_tab:
            try:
                print("kpis_function_tab")
                return kpis_function_tab[file_type.value](files[0]), files[0]
            except Exception as e:
                #pprint(traceback.format_exception(type(e), e, e.__traceback__))
                raise DataGouvException(
                    title="Kpis Function Error",
                    description=f"{str(e)}"
                ) 
    else:
        raise DataGouvException(
            title="Filename Error",
            description=f"Nom de fichier ou type d'actif invalide: {filename}"
        ) 