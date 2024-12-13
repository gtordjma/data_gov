import asyncio
import os
import pprint
import sys
from io import BytesIO
from pathlib import Path

from fastapi import HTTPException, UploadFile
import pandas as pd



#from shared.types.AssetTypes import AssetTypes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .shared.types.AssetTypes import AssetTypes
from .use_cases.UseCase import UseCase
from .use_cases.finance.FinanceRefFile import FinanceRefFile, excel_to_json_data_gov_format

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
        
async def test_ref_file(
        use_case: UseCase,
        file: UploadFile,
        file_asset: AssetTypes,
        file_name: str # ex: REF_CUSTOMERS
    ):
    
    finance_ref_file = FinanceRefFile(
        file=file,  # UploadFile
        file_asset=file_asset,  # ex: LGW
        file_type=file_name,  # ex: DEPOSITS
        use_case=use_case
    )
    try:
        await finance_ref_file.validate_schema()
        print("schema valid")
        print("------------")
        print("gcs path: ", finance_ref_file.get_file_url())
    except Exception as e:
        print(e)

def main():
    # Manque le path pour DL - use FinanceRefFile.get_file_url ??
    #all_json_data_gov_format = excel_to_json_data_gov_format('ref/schema_files_finance.xlsx')
    #specific_asset_json_data_gov_format = excel_to_json_data_gov_format('ref/schema_files_finance.xlsx', AssetTypes.ADL)
    #pprint.pprint(specific_asset_json_data_gov_format)
    #-----------------------------------------------
    file_path = f"test_files/{AssetTypes.LGW.value}/REF_SUPPLIERS.csv"
    upload_file: UploadFile = test_local_file_to_uploadfile(file_path)
    asyncio.run(test_ref_file("finance", upload_file, "LGW", "REF_SUPPLIERS"))


if __name__ == "__main__":
    main()
