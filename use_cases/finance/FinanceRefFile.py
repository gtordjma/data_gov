import importlib
import os
from io import BytesIO
from pathlib import Path
from traceback import print_exc

import pandas as pd
import pandera as pa
from fastapi import UploadFile

from data_gov.shared.CheckFile import validate_file_extension
from data_gov.shared.DataGouvException import DataGouvException
from data_gov.shared.types.AssetTypes import AssetTypes
from data_gov.shared.types.File import File
from data_gov.shared.types.FileStepStatus import FileStepStatus
from data_gov.use_cases.UseCase import UseCase
from data_gov.use_cases.finance.FinanceRefFileTypes import FinanceRefFileTypes

GCP_PROJECT = os.getenv('GCP_PROJECT', 'va-sdh-hq-staging')


def excel_to_df(file_path: str, sheet_name: str):
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_excel(file_path, sheet_name=sheet_name)


def excel_to_json_data_gov_format(file_path: str, file_asset: AssetTypes | None = None,
                                  sheet_name: str = "All files by BU") -> dict:
    df = excel_to_df(file_path, sheet_name)

    grouped_data = {}

    for _, row in df.iterrows():
        asset = row.get("asset")
        is_ref = row.get("is_ref")
        source = row.get("source")
        data_type = row.get("data_type")

        # Check if the row is valid for inclusion
        if is_ref == 1:
            if file_asset is None or asset == file_asset.value:
                if asset not in grouped_data:
                    grouped_data[asset] = []
                grouped_data[asset].append({
                    "source": "",
                    "file_type": data_type,
                    "status": {
                        "loaded": "pending",
                        "checkfile": "pending",
                        "processed": "pending"
                    },
                    "uploaded_by": "",
                    "date": ""
                })

    return grouped_data


def get_file_extension(file: UploadFile):
    file_extension = Path(file.filename).suffix.replace(".", "").lower()
    if not file_extension:
        raise NameError("Could not determine file type from uploaded file.")
    return file_extension


def validate_dataframe_with_schema(df: pd.DataFrame, schema: pa.DataFrameSchema):
    try:
        schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as err:
        print_exc()
        error_message = "The following columns are missing from your file:<br/>"
        for failure in err.failure_cases.itertuples():
            error_message += f"{failure.failure_case}, "
        raise DataGouvException(
            title="Validate Schema Error",
            description=error_message
        )


def get_schema_module(file_asset: AssetTypes, file_type: str):
    schema_module_path = '.'.join(['finance.scripts.references', f'{file_asset.value}.{file_type}', 'schema'])
    try:
        schema_module = importlib.import_module(schema_module_path)
    except ModuleNotFoundError:
        error_message = f"Schema for {'/'.join([file_asset, file_type])} not found."
        raise Exception(error_message)

    return schema_module


def validate_file_schema(df: pd.DataFrame, file_asset: AssetTypes, file_type: str):
    try:
        schema_module = get_schema_module(file_asset, file_type)
        schema: pa.DataFrameSchema | None = getattr(schema_module, 'schema', None)
        if schema is None:
            error_message = f"No schema found in module '{schema_module.__name__}'."
            raise Exception(error_message)
        validate_dataframe_with_schema(df, schema)
    except Exception as e:
        raise DataGouvException(
            title="Validate Schema Error",
            description=f"{str(e)}"
        )


class FinanceRefFile(File):

    def __init__(
            self,
            file: UploadFile,
            file_asset: AssetTypes,
            file_type: FinanceRefFileTypes,
            use_case: UseCase
    ):
        super().__init__(file, file_asset, file_type.value)
        try:
            self.use_case = use_case
            self.file_extension = get_file_extension(file)
            self.status = {
                'loaded': FileStepStatus.FINISHED,
                'checkfile': FileStepStatus.FINISHED,
                'processed': FileStepStatus.PENDING
            }
        except DataGouvException as e:
            print(e)
            raise e

    def get_file_url(self):
        mime = validate_file_extension(self.file)
        return f"gs://{GCP_PROJECT}-safe/{self.use_case}/references/{self.file_asset.value}/{self.file_asset.value}_{self.file_type}.{mime}"

    async def df_from_file(self):
        try:
            module_path = f'finance.scripts.references.{self.file_asset.value}.{self.file_type}.read'
            content = await self.file.read()
            content = BytesIO(content)
            read_module = importlib.import_module(module_path)
            read_function = getattr(read_module, 'read')
            df = read_function(content, nrows=1000)
            return df
        except Exception as e:
            print_exc()
            raise DataGouvException(
                title="Load Dataset Error",
                description=f"Le fichier envoyé ne correspond pas pour l'asset {self.file_asset.value} et le type {self.file_type}.\nErreur détaillé: {str(e)}"
            )

    async def validate_schema(self):
        df = await self.df_from_file()
        validate_file_schema(df, self.file_asset, self.file_type.replace("_", ""))

    def update_status(self, k, v):
        self.status[k] = v

    def get_status(self):
        return self.status
