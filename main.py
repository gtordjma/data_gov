import asyncio
from fastapi import UploadFile
from pathlib import Path
from io import BytesIO

import sys
import os

sys.path.append(os.path.abspath("airports_finances"))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_gov.finance_file import FinanceFile
from data_gov.ingestion.process import process_file
from data_gov.types import AssetTypes, FileStepStatus

def test_local_file_to_uploadfile(file_path: str) -> UploadFile:
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

async def test_file(file_path: str):
    upload_file = test_local_file_to_uploadfile(file_path)
    
    finance_file = FinanceFile(
        file=upload_file, # UploadFile
        file_asset=AssetTypes.LGW, # ex: LGW
        file_type="DEPOSITS", # ex: DEPOSITS
        year="2024", # ex: 2024
        month="08", # ex: 08
        file_version=None # ex: B0 | None
    )
    file_name, running_date, file_path = await finance_file.save_file_to_tmp_folder()
    kpis, parquet_file_path = process_file(file_name, running_date, file_path)
    print("kpis, parquet_file_path", kpis, parquet_file_path)
    finance_file.update_status("checkKpis", FileStepStatus.RUNNING)
    print(finance_file.status)
    
def main():
    file_path = "test_files/LGW_FINANCE_DEPOSITS_2024-08-31 (1).csv"
    asyncio.run(test_file(file_path))

if __name__ == "__main__":
        main()