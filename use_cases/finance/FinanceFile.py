from pathlib import Path
from typing import Optional

from fastapi import UploadFile

from ...shared.DataGouvException import DataGouvException
from ...shared.types.AssetTypes import AssetTypes
from ...shared.types.File import File
from ...shared.types.FileStepStatus import FileStepStatus
from ...use_cases.finance.FinanceFileTypes import FinanceFileTypes
from ...use_cases.finance.FinanceVersions import FinanceVersions
from ...use_cases.finance.Utils import get_sources, get_last_day
from ...shared.CheckFile import validate_file_extension


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
        
    def get_running_date(self):
        return f"{self.year}-{self.month}-{get_last_day(self.month, self.year)}"

    async def save_file_to_tmp_folder(self) -> tuple[str, str, Path]:
        try:
            # Validate and prepare file_asset and file_version
            file_asset_value = self.file_asset.value if not isinstance(self.file_asset, str) else self.file_asset
            file_version_value = self.file_version.value if self.file_version and not isinstance(self.file_version, str) else self.file_version

            mime = validate_file_extension(self.file)
            running_date = self.get_running_date()
            
            if file_version_value:
                file_name = f"{file_asset_value}_FINANCE_{self.file_type}_{file_version_value}_{running_date}.{mime}"
            else:
                file_name = f"{file_asset_value}_FINANCE_{self.file_type}_{running_date}.{mime}"
            
            # TODO to save directly to raw
            file_path = Path(__file__).parent.parent.parent / "saved_file_local" / file_name
            with open(file_path, "wb") as buffer:
                content = await self.file.read()
                buffer.write(content)
            return file_name, running_date, file_path
        except DataGouvException as e:
            print(e)
            raise e
        except Exception as e:
            print(e)
            raise DataGouvException(
                title="Internal Error",
                description="Internal error: saving the tmp file has failed. Please contact support."
            )

    def update_status(self, k, v):
        self.status[k] = v

    def get_status(self):
        return self.status
