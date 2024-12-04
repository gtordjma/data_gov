from datetime import datetime

from data_gov.shared.types.AssetTypes import AssetTypes


class ParquetFile:
    def __init__(self, asset: AssetTypes, use_case: str, file_name: str, file_source: str, parquet_file_path: str,
                 classic_file_path: str | None):
        self.asset = asset
        self.use_case = use_case
        self.file_name = file_name
        self.file_source = file_source
        self.parquet_file_path = parquet_file_path
        self.classic_file_path = classic_file_path
        self.timestamp = datetime.now()
