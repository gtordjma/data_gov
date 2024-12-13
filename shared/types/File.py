from fastapi import UploadFile

from .AssetTypes import AssetTypes


class File:
    def __init__(self, file: UploadFile, file_asset: AssetTypes, file_type: str):
        self.file = file
        self.file_asset = file_asset
        self.file_type = file_type
