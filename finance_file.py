from pathlib import Path
from typing import Optional

from fastapi import UploadFile

from data_gov.ingestion.check_file import validate_filename_type, validate_mime_type
from data_gov.ingestion.utils import get_last_day


from data_gov.types import AssetTypes, FileStepStatus, Versions
from data_gov.error import DataGouvException


class FinanceFile:
    def __init__(
        self,
        file: UploadFile,
        file_asset: AssetTypes,
        file_type: str,
        year: str,
        month: str, 
        file_version: Optional[Versions]
    ):
        try:
            self.file = file
            self.file_asset = file_asset
            self.file_type = file_type
            self.year = year
            self.month = month
            self.file_version = file_version
            self.file_type_enum = validate_filename_type(file_type)
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
            mime = validate_mime_type(self.file)
            running_date = f"{self.year}-{self.month}-{get_last_day(self.month, self.year)}"
            file_name = f"{self.file_asset.value}_FINANCE_{self.file_type_enum.value}_{running_date}.{mime}"
            file_path = Path("saved_file_local") / file_name
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
        

        
# finance_file = FinanceFile(
#         file=file # UploadFile
#         file_asset=file_asset, # ex: LGW
#         file_type=file_type, # ex: DEPOSITS
#         year=year, # ex: 2024
#         month=month, # ex: 08
#         file_version= file_version # ex: B0
#     )