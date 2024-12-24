
import asyncio

from .ingestion import clean_final_data, update_data_template

from ..use_cases.finance.Utils import get_ingestion_template_data
from .utils.quality import get_quality_data_formatted_from_ingestion
from .types import UseCases, AssetTypes


class DataFilePipeline():
    def __init__(
            self,
            use_case,
            asset: AssetTypes.AssetTypes,
            year,
            month
    ):
        self.year = year
        self.month = month
        self.use_case = use_case
        self.asset = asset
        self.quality_data = []

    async def initialize(self, tmp_parquet_files_dict):
        quality_data, template_data = await asyncio.gather(
            get_quality_data_formatted_from_ingestion(
                self.use_case, 
                self.asset.value, 
                self.year, 
                self.month
                ),
            get_ingestion_template_data(self.asset.value)
        )
        updated_template = await update_data_template(
            tmp_parquet_files_dict,
            template_data,
            quality_data,
            self.year,
            self.month,
            self.asset,
            self.use_case
        )
        return clean_final_data(updated_template)
        return {}