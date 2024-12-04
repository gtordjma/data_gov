from pathlib import Path
from typing import Optional

from fastapi import UploadFile

from data_gov.shared.CheckFile import validate_file_extension
from data_gov.shared.DataGouvException import DataGouvException
from data_gov.shared.types.AssetTypes import AssetTypes
from data_gov.shared.types.File import File
from data_gov.shared.types.FileStepStatus import FileStepStatus
from data_gov.use_cases.finance.FinanceFileTypes import FinanceFileTypes
from data_gov.use_cases.finance.FinanceVersions import FinanceVersions
from data_gov.use_cases.finance.Utils import get_sources, get_last_day


class FinanceFile(File):
    def __init__(
            self,
            file: UploadFile,
            file_asset: AssetTypes,
            file_type: str,
            year: str,
            month: str,
            file_version: Optional[FinanceVersions]
    ):
        super().__init__(file, file_asset, file_type)
        try:
            self.year = year
            self.month = month
            self.file_version = file_version
            self.sources = [FinanceFileTypes[item.upper()] for item in get_sources(self.file_asset, self.file_type)]
            self.status = {
                'loaded': FileStepStatus.FINISHED,
                'checkfile': FileStepStatus.FINISHED,
                'checkKpis': FileStepStatus.PENDING,
                'processed': FileStepStatus.PENDING
            }
        except DataGouvException as e:
            print(e)
            raise e

    async def save_file_to_tmp_folder(self) -> tuple[str, str, Path]:
        try:
            mime = validate_file_extension(self.file)
            running_date = f"{self.year}-{self.month}-{get_last_day(self.month, self.year)}"
            if self.file_version:
                file_name = f"{self.file_asset.value}_FINANCE_{self.file_type}_{self.file_version.value}_{running_date}.{mime}"
            else:
                file_name = f"{self.file_asset.value}_FINANCE_{self.file_type}_{running_date}.{mime}"
            # TODO to save  directecly to raw
            file_path = Path(__file__).parent.parent.parent / "saved_file_local" / file_name
            with open(file_path, "wb") as buffer:
                content = await self.file.read()
                buffer.write(content)
            return file_name, running_date, file_path
        except DataGouvException as e:
            print(e)
            raise e
        except Exception as e:
            raise DataGouvException(
                title="Internal Error",
                description="Internal error: saving the tmp file has failed. Please contact support."
            )

    def update_status(self, k, v):
        self.status[k] = v

    def get_status(self):
        return self.status
