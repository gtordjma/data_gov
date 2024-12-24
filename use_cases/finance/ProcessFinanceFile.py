import importlib
from traceback import print_exc

import pandas as pd
import pandera as pa
from fastapi import UploadFile

from ...shared.utils.gcp import insert_file_into_tmp_bucket
from ...shared.DataGouvException import DataGouvException
from ...shared.types.AssetTypes import AssetTypes
from .FinanceFileTypes import FinanceFileTypes
from .KpisFunctions import kpis_function_tab
from .Utils import copy_to_directories
from .submodule.finance.scripts.ProcessingFunction import processing_function

assets_module_path = "data_gov.use_cases.finance.submodule.finance.scripts.assets"

def load_dataset(filepath: UploadFile | str, file_type: str, asset_type: AssetTypes) -> pd.DataFrame:
    try:
        module_path = f'{assets_module_path}.{asset_type.value.upper()}.{file_type.lower()}.read'
        read_module = importlib.import_module(module_path)
        read_function = getattr(read_module, 'read')
        df = read_function(filepath, nrows=1000)
        return df
    except Exception as e:
        print_exc()
        raise DataGouvException(
            title="Load Dataset Error",
            description=f"The file sent does not match for asset {asset_type.value} and type {file_type}.<br/>Please check the contents of your file."
        )


def get_schema_module(file_asset: AssetTypes, file_type: str):
    schema_module_path = '.'.join([assets_module_path, file_asset.value.upper(), file_type, 'schema'])

    try:
        schema_module = importlib.import_module(schema_module_path)
    except ModuleNotFoundError:
        raise Exception(f"Le schéma pour {'/'.join([file_asset.value.lower(), file_type])} n'a pas été trouvé.")

    return schema_module


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


def validate_file_schema(filepath: str, file_asset: AssetTypes, file_type: FinanceFileTypes):
    df = load_dataset(filepath, file_type.value.lower(), file_asset)
    schema_module = get_schema_module(file_asset, file_type.value.lower())
    schema: pa.DataFrameSchema | None = getattr(schema_module, 'schema', None)
    if schema is None:
        raise Exception(f"Aucun schéma trouvé dans le module '{schema_module.__name__}'.")

    # df, schema = transform_dataframe_for_kap(df, schema, func_name)

    validate_dataframe_with_schema(df, schema)


def process_file(filename, running_date: str, filepath: str, file_type: FinanceFileTypes, file_asset: AssetTypes):
    """
    Processus complet de traitement d'un fichier valide.
    """

    if file_type and file_asset:
        # Valider le schéma
        validate_file_schema(filepath, file_asset, file_type)

        copy_to_directories(filepath, file_asset, file_type)

        try:
            files = processing_function(file_asset.value, file_type.value, running_date)
        except Exception as e:
            raise DataGouvException(
                title="Processing Function Error",
                description=f"{str(e)}"
            )
            
        parquet_file_path = files[0]
        insert_file_into_tmp_bucket(file_asset, "finance", filename, file_type.value, parquet_file_path)

        if file_type in kpis_function_tab:
            try:
                print("kpis_function_tab")
                return kpis_function_tab[file_type](parquet_file_path), parquet_file_path
            except Exception as e:
                raise DataGouvException(
                    title="Kpis Function Error",
                    description=f"{str(e)}"
                )
        else:
            print('no kpis_function_tab')
            return {"no_kpis_function": [[""],[""]]}, parquet_file_path
    else:
        raise DataGouvException(
            title="Filename Error",
            description=f"Nom de fichier ou type d'actif invalide: {filename}"
        )


def generate_check_ref_messages(data):
    messages = []
    mapping_error = False

    for key, value in data.items():
        if isinstance(value, dict):
            for column, ids in value.items():
                if ids:  # Vérifie si le tableau est vide
                    msg = f"The file you just uploaded contains IDs that are not mapped with the reference file {key} in the {column} column.<br/>The following IDs are not mapped: {ids}."
                    if 'MAPPING_LOCAL'in msg:
                        msg += "<br/>Please resolve these mappings then you can upload your file again."
                    messages.append(msg)

    if any('MAPPING_LOCAL' in message for message in messages):
        raise DataGouvException(
            title="Ref Check Function Error",
            description=f"{'<br/><br/>'.join(messages)}"
        )

    return messages

def get_check_ref_data(filename, filepath: str, file_type: FinanceFileTypes, file_asset: AssetTypes):
    """
    Processus complet de traitement d'un fichier valide.
    """
    try:
        schema_module = importlib.import_module(f"{assets_module_path}.{file_asset.value}.{file_type.value.lower()}.check_refs")
        return schema_module.check_refs(filepath)
    except ModuleNotFoundError as e:
        print_exc()
        return None
    except AttributeError as e:
        print_exc()
        return None
    except Exception as e:
        raise DataGouvException(
            title="Ref Check Function Error",
            description=f"{str(e)}"
        )
        
def get_check_ref_messages(filename, filepath: str, file_type: FinanceFileTypes, file_asset: AssetTypes) -> tuple[list, bool]:
    check_ref_data = get_check_ref_data(filename, filepath, file_type, file_asset)
    if check_ref_data is None:
        return []
    return generate_check_ref_messages(check_ref_data)