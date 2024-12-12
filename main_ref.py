import asyncio
import os
import sys
from io import BytesIO
from pathlib import Path

from fastapi import UploadFile

from data_gov.use_cases.finance.FinanceRefFileTypes import FinanceRefFileTypes

# from shared.types.AssetTypes import AssetTypes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_gov.shared.types.AssetTypes import AssetTypes
from data_gov.use_cases.UseCase import UseCase
from data_gov.use_cases.finance.FinanceRefFile import FinanceRefFile


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
        file_name: FinanceRefFileTypes  # ex: REF_CUSTOMERS
):
    finance_ref_file = FinanceRefFile(
        file=file,  # UploadFile
        file_asset=file_asset,  # ex: LGW
        file_type=file_name,  # ex: DEPOSITS
        use_case=use_case
    )
    print(file_name, file_asset, ':', sep='  ')
    await finance_ref_file.validate_schema()
    # print("------------")

    print("schema valid")
    print("gcs path: ", finance_ref_file.get_file_url())
    print("------------")


def main():
    # Manque le path pour DL - use FinanceRefFile.get_file_url ??
    # all_json_data_gov_format = excel_to_json_data_gov_format('ref/schema_files_finance.xlsx')
    # specific_asset_json_data_gov_format = excel_to_json_data_gov_format('ref/schema_files_finance.xlsx')
    # pprint.pprint(specific_asset_json_data_gov_format)
    # -----------------------------------------------

    ref_files = {
        # AssetTypes.ADL: [
        #     [FinanceRefFileTypes.MAPPINGCAPEX, "ADL_MAPPINGCAPEX.xlsx"],
        #     [FinanceRefFileTypes.MAPPINGCLIENTSIATA, "ADL_MAPPINGCLIENTSIATA.xlsx"],
        #     [FinanceRefFileTypes.REFCUSTOMERS, "ADL_REFCUSTOMERS.csv"],
        #     [FinanceRefFileTypes.REFSUPPLIERS, "ADL_REFSUPPLIERS.csv"],
        # ],
        # AssetTypes.AERODOM: [
        #     [FinanceRefFileTypes.MAPPINGCOSTCENTER, "AERODOM_MAPPINGCOSTCENTER.xlsx"],
        #     [FinanceRefFileTypes.MAPPINGAIRPORTS, "AERODOM_MAPPINGAIRPORTS.xlsx"],
        # ],
        # AssetTypes.AGO: [
        #     [FinanceRefFileTypes.MAPPINGACTIVITIES, "AGO_MAPPINGACTIVITIES.xlsx"],
        #     [FinanceRefFileTypes.MAPPINGAIRPORTS, "AGO_MAPPINGAIRPORTS.xlsx"],
        #     [FinanceRefFileTypes.MAPPINGCLIENTSIATA, "AGO_MAPPINGCLIENTSIATA.csv"],
        #     [FinanceRefFileTypes.MAPPINGCOMPTESBUDGET, "AGO_MAPPINGCOMPTESBUDGET.xlsx"],
        # ],
        # AssetTypes.ANA: [
        #     [FinanceRefFileTypes.MAPPINGCOSTCENTER, "ANA_MAPPINGCOSTCENTER.xlsx"]
        # ],
        # AssetTypes.BEG: [
        #     [FinanceRefFileTypes.MAPPINGCLIENTSIATA, "BEG_MAPPINGCLIENTSIATA.xlsx"],
        #     [FinanceRefFileTypes.REFCUSTOMERS, "BEG_REFCUSTOMERS.XLSX"],
        # ],
        # AssetTypes.BFS: [
        #     [FinanceRefFileTypes.REFCUSTOMERS, "BFS_REFCUSTOMERS.xlsx"]
        # ],
        # AssetTypes.KAP: [
        #     [FinanceRefFileTypes.MAPPINGCAPEX, "KAP_MAPPINGCAPEX.xlsx"],
        #     [FinanceRefFileTypes.MAPPINGCOSTCENTER, "KAP_MAPPINGCOSTCENTER.xlsx"],
        #     [FinanceRefFileTypes.MAPPINGENTITIES, "KAP_MAPPINGENTITIES.xlsx"],
        # ],
        # AssetTypes.LGW: [
        #     [FinanceRefFileTypes.REFCUSTOMERS, "LGW_REFCUSTOMERS.csv"],
        #     [FinanceRefFileTypes.REFSUPPLIERS, "LGW_REFSUPPLIERS.csv"],
        # ],
        # AssetTypes.LIR: [
        #     [FinanceRefFileTypes.MAPPINGCOSTCENTER, "LIR_MAPPINGCOSTCENTER.xlsx"]
        # ],
        AssetTypes.OMA: [
            [FinanceRefFileTypes.MAPPINGAIRPORTS, "OMA_MAPPINGAIRPORTS.xlsx"],
            [FinanceRefFileTypes.MAPPINGCAPEXCATEGORY, "OMA_MAPPINGCAPEXCATEGORY.xlsx"],
            [FinanceRefFileTypes.MAPPINGCLIENTSIATA, "OMA_MAPPINGCLIENTSIATA.xlsx"],
            [FinanceRefFileTypes.MAPPINGCOSTCENTER, "OMA_MAPPINGCOSTCENTER.xlsx"],
        ],
        AssetTypes.SCA: [
            [FinanceRefFileTypes.MAPPINGCOSTCENTER, "SCA_MAPPINGCOSTCENTER.xlsx"]
        ],
        AssetTypes.SCL: [
            [FinanceRefFileTypes.REFCUSTOMERS, "SCL_REFCUSTOMERS.xlsx"]
        ],
        AssetTypes.SSA: [
            [FinanceRefFileTypes.MAPPINGAIRPORTS, "SSA_MAPPINGAIRPORTS.xlsx"],
            [FinanceRefFileTypes.MAPPINGCAPEX, "SSA_MAPPINGCAPEX.xlsx"],
            [FinanceRefFileTypes.MAPPINGCOSTCENTER, "SSA_MAPPINGCOSTCENTER.xlsx"],
            [FinanceRefFileTypes.REFCUSTOMERS, "SSA_REFCUSTOMERS.xlsx"],
        ],

    }
    for asset, files in ref_files.items():
        for file in files:
            upload_file: UploadFile = test_local_file_to_uploadfile(f"./test_files/refs/{asset.value}/{file[1]}")
            asyncio.run(test_ref_file("finance", upload_file, asset, file[0]))


if __name__ == "__main__":
    main()
