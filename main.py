import asyncio
import pprint
from fastapi import UploadFile
from pathlib import Path
from io import BytesIO

import sys
import os

sys.path.append(os.path.abspath("airports_finances"))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_gov.finance_file import FinanceFile
from data_gov.ingestion.process import process_file
from data_gov.types import AssetTypes, FileStepStatus, Versions

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

async def test_file(
    file: UploadFile,
    file_asset: AssetTypes,
    file_type: str,
    file_version: Versions | None,
    year: str,
    month: str,
):
    
    file_asset: AssetTypes = AssetTypes.LGW
    finance_file = FinanceFile(
        file=file, # UploadFile
        file_asset=file_asset, # ex: LGW
        file_type=file_type, # ex: DEPOSITS
        year=year, # ex: 2024
        month=month, # ex: 08
        file_version=file_version # ex: B0 | None
    )
    file_name, running_date, file_path = await finance_file.save_file_to_tmp_folder()
    kpis, parquet_file_path = process_file(file_name, running_date, file_path)
    pprint.pprint(kpis)
    print("parquet_file_path", parquet_file_path)
    finance_file.update_status("checkKpis", FileStepStatus.RUNNING)
    print(finance_file.status)
    

def main():
    file_path = "test_files/LGW_FINANCE_DEPOSITS_2024-08-31 (1).csv"
    upload_file: UploadFile = test_local_file_to_uploadfile(file_path)
    asyncio.run(test_file(upload_file, AssetTypes.LGW, "DEPOSITS", None, "2024", "11"))

if __name__ == "__main__":
        main()