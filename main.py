import asyncio
import os
import sys
from io import BytesIO
from pathlib import Path

from fastapi import UploadFile

from .use_cases.UseCase import UseCase
from .use_cases.finance.FinanceFile import FinanceFile
from .use_cases.finance.FinanceVersions import FinanceVersions
from .use_cases.finance.ProcessFinanceFile import process_file
from .use_cases.finance.ProcessFinanceFile import check_ref

# sys.path.append(os.path.abspath("airports_finances"))
# sys.path.append(os.path.abspath('use_cases/finance/submodule'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .shared.types.AssetTypes import AssetTypes
from .shared.types.FileStepStatus import FileStepStatus


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
        file_version: FinanceVersions | None,
        year: str,
        month: str,
):
    finance_file = FinanceFile(
        file=file,  # UploadFile
        file_asset=file_asset,  # ex: LGW
        file_type=file_type,  # ex: DEPOSITS
        year=year,  # ex: 2024
        month=month,  # ex: 08
        file_version=file_version  # ex: B0 | None
    )
    file_name, running_date, file_path = await finance_file.save_file_to_tmp_folder()

    for file_type_source in finance_file.sources:
        print('Processing : ', file_type_source, file_asset, file_path)
        check_ref_results = check_ref(file_name, file_path, file_type_source, file_asset)
        print(check_ref_results)
        # kpis, parquet_file_path = process_file(file_name, running_date, file_path, file_type_source, file_asset)
        # pprint.pprint(kpis)
        # finance_file.update_status("checkKpis", FileStepStatus.RUNNING)
        # print(finance_file.status)


def main():
    files = {
        AssetTypes.AERODOM: [
            ["BUDGET", "AERODOM_FINANCE_BUDGET_R2_2024-06-30.xlsx", FinanceVersions.R2],
            ["CAPEX", "AERODOM_FINANCE_CAPEX_2024-08-31.xlsx", None],
            ["CPXFORECAST", "AERODOM_FINANCE_CPXFORECAST_R2_2024.xlsx", FinanceVersions.R2],
            ["GENERAL_LEDGER", "AERODOM_FINANCE_GL_2024-10-31 (1).xlsx", None],
            ["MAPPING_LOCAL", "AERODOM_FINANCE_MAPPINGLOCAL_2022-09-26 (1).xlsx", None],
            ["PROCUREMENTS", "AERODOM_FINANCE_PROCUREMENTS_2024-10-31 (1).xlsx", None],
            ["PROVISIONS", "AERODOM_FINANCE_PROVISIONS_GUARANTEES_DEPOSITS_2024-09-30.xlsx", None],
            ["RECEIVABLES", "AERODOM_FINANCE_RECEIVABLES_2024-10-31.xlsx", None],
        ],
        AssetTypes.LGW: [
            ["BUDGET", "LGW_FINANCE_BUDGET_B02025_2024-10-21.csv", FinanceVersions.B0],
            ["CAPEX", "LGW_FINANCE_CAPEX_ACTUAL_October032024_084754.csv", None],
            ["CPXFORECAST", "LGW_FINANCE_CAPEX_B02024_2024_08_15 (1).csv", FinanceVersions.B0],
            ["CUSTOMER", "LGW_FINANCE_CUSTOMER_2024-11-30.csv", None],
            ["DEPOSITS", "LGW_FINANCE_DEPOSITS_2024-11-30.csv", None],
            ["GENERAL_LEDGER", "LGW_FINANCE_GL_ACTUAL_November112024_095423.csv", None],
            ["GUARANTEES", "LGW_FINANCE_GUARANTEES_2024-11-30.csv", None],
            ["MAPPING_LOCAL", "LGW_FINANCE_MAPPINGLOCAL_February122024_091554.csv", None],
            ["MAPPING_USECASE", "LGW_FINANCE_MAPPINGUSECASE_2023-10-18.xlsx", None],
            ["PROCUREMENTS", "LGW_FINANCE_PROCUREMENTS_2024_10_31.csv", None],
            ["PROVISIONS", "LGW_FINANCE_PROVISIONS_2024-11-30.csv", None],
            ["RECEIVABLES", "LGW_FINANCE_RECEIVABLES_2024_10_31.csv", None],
        ],
        AssetTypes.LIR: [
            ["BUDGET", "LIR_FINANCE_BUDGET_R1_2024-05-01.xlsx", FinanceVersions.R1],
            ["DEPOSITS", "LIR_FINANCE_DEPOSITS_2024-10-31.xlsx", None],
            ["GENERAL_LEDGER", "LIR_FINANCE_GL_2024-10-31.xlsx", None],
            ["GUARANTEES", "LIR_FINANCE_GUARANTEES_2024-07-31.xlsx", None],
            ["MAPPING_LOCAL", "LIR_FINANCE_MAPPINGLOCAL_2024-01-31.xlsx", None],
            ["PROCUREMENTS", "LIR_FINANCE_PROCUREMENTS_2024-10-31.xls", None],
            ["PROVISIONS", "LIR_FINANCE_PROVISIONS_2024-10-31.xlsx", None],
            ["RECEIVABLES", "LIR_FINANCE_RECEIVABLES_2024-10-31.xls", None],

        ],
        AssetTypes.ANA: [
            ["BUDGET", "ANA_FINANCE_BUDGET_R32023_2023-10-31.CSV", FinanceVersions.R3],
            ["CAPEX", "ANA_FINANCE_CAPEX_2024-10-31.xlsx", None],
            ["GENERAL_LEDGER", "ANA_FINANCE_GL_2024-10-31.csv", None],
            ["MAPPING_LOCAL", "ANA_FINANCE_MAPPINGLOCAL_2024-05-17 (1).xlsx", None],
            ["PROCUREMENTS", "ANA_FINANCE_PROCUREMENTS_2024-10-31.csv", None],
            ["RECEIVABLES", "ANA_FINANCE_RECEIVABLES_2024-10-31.csv", None],
        ],

        AssetTypes.SCA: [
            ["BUDGET", "SCA_FINANCE_BUDGET_B0 2025_2024-11-01.csv", FinanceVersions.R2],
            ["CAPEX", "SCA_FINANCE_CAPEX_2024-11-30.xlsx", None],
            ["CPXFORECAST", "SCA_FINANCE_CPXFORECAST_R22024_2024-07-31.xlsx", FinanceVersions.R2],
            ["CUSTOMER", "SCA_FINANCE_CUSTOMER_2024-11-30.xlsx", None],
            ["GENERAL_LEDGER", "SCA_FINANCE_GL_2024-11-30.xlsx", None],
            ["MAPPING_LOCAL", "SCA_FINANCE_MAPPINGLOCAL_2024-01-29 (1).xlsx", None],
            ["PROCUREMENTS", "SCA_FINANCE_PROCUREMENTS_PNH&KOS_2024-11-30.xlsx", None],
            ["PROVISIONS", "SCA_FINANCE_PROVISIONS_2024-11-30.xlsx", None],
            ["RECEIVABLES", "SCA_FINANCE_RECEIVABLES_KOS_2024-10-31.xlsx", FinanceVersions.KOS],
            # TODO Cas particulier : il faut renomme lors du move du safe pour pas ecrasement (<version>_output.parquet)
            ["RECEIVABLES", "SCA_FINANCE_RECEIVABLES_PNH_2024-10-31.xlsx", FinanceVersions.PNH],
            # TODO Cas particulier : il faut renomme lors du move du safe pour pas ecrasement (<version>_output.parquet)
        ],

        AssetTypes.AGO: [
            ["BUDGET", "AGO_FINANCE_BUDGET_R3_2023-12-31.csv", FinanceVersions.R3],
            ["GUARANTEES", "AGO_FINANCE_D&G_2024-06-30 (2).csv", None],
            ["GENERAL_LEDGER", "AGO_FINANCE_GL_2024-09-30.csv", None],
            ["MAPPING_LOCAL", "AGO_FINANCE_MAPPINGLOCAL_2023-02-16 (1).xlsx", None],
            ["PROCUREMENTS", "AGO_FINANCE_PROCUREMENTS_2024-09-30.csv", None],
            ["PROVISIONS", "AGO_FINANCE_PROVISIONS_2024-06-30.csv", None],
            ["RECEIVABLES", "AGO_FINANCE_RECEIVABLES_2024-09-30.csv", None],
        ],
        AssetTypes.KAP: [
            ["CUSTOMER", "Customer Revenues 2024 10.xlsx", None],
            ["DEPOSITS", "Deposits 2024 09.xlsx", None],
            ["GENERAL_LEDGER", "FY24 Actual V07 Apr-Oct.xlsx", None],
            ["BUDGET", "FY24 Budget R3.xlsx", FinanceVersions.R3],
            ["GUARANTEES", "Guaranties 2024 09.xlsx", None],
            ["PROCUREMENTS", "Procurements 2024 10.xlsx", None],
            ["PROVISIONS", "Provisions 2024 09.xlsx", None],
            ["RECEIVABLES", "Receivables 2024 10.xlsx", None],
            ["MAPPING_LOCAL", "SDH Finance P&L Mapping 15.10.24.xlsx", None],
            ["SUPPLIER", "Supplier OPEX 2024 10.xlsx", None],
        ],
        AssetTypes.ADL: [
            ["CAPEX", "ADL_FINANCE_CAPEX_2024-06-30.xlsx", None],
            ["CPXFORECAST", "ADL_FINANCE_CAPEX_2024-R1.xlsx", FinanceVersions.B0],
            ["CUSTOMER", "ADL_FINANCE_CUSTOMER_2024-10-31.csv", None],
            ["GENERAL_LEDGER", "ADL_FINANCE_GL_2024-06-30.xlsx", None],
            ["BUDGET", "ADL_FINANCE_GL_2024-R1.xlsx", FinanceVersions.R1],
            ["MAPPING_LOCAL", "ADL_FINANCE_MAPPINGLOCAL_2023-04-12 (2).xlsx", None],
            ["PROCUREMENTS", "ADL_FINANCE_PROCUREMENTS_2024-08-31.csv", None],
            ["RECEIVABLES", "ADL_FINANCE_RECEIVABLES_2024-10-31 (1).csv", None],
            ["SUPPLIER", "ADL_FINANCE_SUPPLIER_2024-08-31.csv", None],
        ],
        AssetTypes.BEG: [
            ["CAPEX", "BEG_FINANCE_CAPEX_ACTUAL_2024-10-31.xlsx", None],
            ["CPXFORECAST", "BEG_FINANCE_CPXFORECAST_B02025.xlsx", FinanceVersions.B0],
            ["DEPOSITS", "BEG_FINANCE_DEPOSITS_2024 10 31.XLSX", None],
            ["GENERAL_LEDGER", "BEG_FINANCE_GL_ACTUAL_2024-10-31.xlsx", None],
            ["MAPPING_LOCAL", "BEG_FINANCE_MAPPINGLOCAL_2024-09-30.xlsx", None],
            ["GUARANTEES", "BEG_FINANCE_PNOTES_GUARANTEES_2024 10 31.XLSX", None],
            ["PROCUREMENTS", "BEG_FINANCE_PROCUREMENTS_2024-10-31.XLSX", None],
            ["PROVISIONS", "BEG_FINANCE_PROVISIONS_2024 09 30.xlsx", None],
            ["RECEIVABLES", "BEG_FINANCE_RECEIVABLES_2024 10 31.XLSX", None],
        ],
        AssetTypes.SCL: [
            ["CUSTOMER", "SCL_FINANCE_CUSTOMER_2024-10-31 (002).xlsx", None],
            ["GENERAL_LEDGER", "SCL_FINANCE_GL_2024-09-30.xlsx", None],
            ["PROVISIONS", "SCL_FINANCE_PROVISIONS_GUARANTEES_DEPOSITS_2024-10-31.xlsx", None],
            ["RECEIVABLES", "SCL_FINANCE_RECEIVABLES_2024-10-31.xlsm", None],
        ],
        AssetTypes.BFS: [
            ["RECEIVABLES", "BFS AR 09.24 Customer ageing trans date.csv", None],
            ["BUDGET", "BFS_FINANCE_BUDGET_B02024_2024-01-31.csv", FinanceVersions.B0],
            ["GENERAL_LEDGER", "BFS_FINANCE_GL_ACTUAL_2024_07_31 (1).csv", None],
            ["MAPPING_LOCAL", "BFS_FINANCE_MAPPINGLOCAL_2023-06-06 (1).xlsx", None],
        ],
        AssetTypes.OMA: [
            ["RECEIVABLES", "finance_OMA_AR_OMA_FINANCE_RECEIVABLES_2024-04-30.xlsx", None],
            ["PROCUREMENTS", "Proveedores consolidados agosto 2023 VINCIv2.XLSX", None],
            ["GENERAL_LEDGER", "sftp_oma_finance_input_gl_SAP_FINANCE_GL_2024_10_10_150057.csv", None],
            ["MAPPING_LOCAL", "OMA_FINANCE_MAPPINGLOCAL_2023-11-15 (1).xlsx", None]
        ],
        AssetTypes.CVA: [
            ["RECEIVABLES", "CVAiports - ERP Account Receivables_06.09.2024.xlsx", None],

        ],
        AssetTypes.SSA: [  # SSA & AMA cas particulier #TODO lors du move en safe il faut prend SSA & AMA
            ["RECEIVABLES", "AMA_FINANCE_RECEIVABLES_2024-09-30.xlsx", FinanceVersions.AMA],
            ["RECEIVABLES", "SSA_FINANCE_RECEIVABLES_2024-09-30.xlsx", FinanceVersions.SSA],
            ["BUDGET", "SSA_FINANCE_BUDGET_R32023_2023-12-31.xlsx", FinanceVersions.R3],
            ["CAPEX", "SSA_FINANCE_CAPEX_2024-08-31.xlsx", None],
            ["CPXFORECAST", "SSA_FINANCE_CPXFORECAST_B02023_2023-04-06.xlsx", FinanceVersions.B0],
            ["GENERAL_LEDGER", "SSA_FINANCE_GL_2024-09-30.xlsx", None],
            ["MAPPING_LOCAL", "SSA_FINANCE_MAPPINGLOCAL_2024-09-04.xlsx", None],
            ["PROCUREMENTS", "SSA_FINANCE_PROCUREMENTS_2024-08-31.xlsx", None],
        ],

    }
    for asset in files.keys():
        for file in files[asset]:
            file_path = f"test_files/{asset.value}/{file[1]}"
            upload_file: UploadFile = test_local_file_to_uploadfile(file_path)
            asyncio.run(test_file(upload_file, asset, file[0], file[2], "2024", "11"))


if __name__ == "__main__":
    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Mohamed KHEY\workplace\1- Vinci Airport Projects\ALL_SECRECTS\va-sdh-hq-staging-mohamed_khey.json"

    main()
