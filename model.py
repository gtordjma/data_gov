from enum import Enum
from pydantic import BaseModel, Field, RootModel, root_validator, validator
from typing import Any, List, Dict, Optional, Union

from data_gov.types import AssetTypes, FileTypes

def is_valid_combination(value: str) -> bool:
    parts = value.split("_")

    if len(parts) < 3 or parts[-1] != 'loadfiles':
        return False

    asset_type_str = parts[0].upper()
    file_type_str = "_".join(parts[1:-1])

    if asset_type_str not in AssetTypes.__members__:
        return False

    if file_type_str not in [ft.value for ft in FileTypes]:
        return False

    return True

class Alignment(BaseModel):
    version: Optional[str] = None
    airportIATACode: Optional[str] = None
    accountingDate: Optional[str] = None
    accountId: Optional[str] = None
    activityId: Optional[str] = None
    costCode: Optional[str] = None
    reporting: Optional[str] = None
    amountValue: Optional[str] = None
    clientSupplId: Optional[str] = None
    extractDate: Optional[str] = None

FilenameContains = Enum(
    'FilenameContains', 
    {
        name.replace('FINANCE_', '').upper(): name.replace('FINANCE_', '').upper()
        for name in FileTypes.__members__
    }
)

class SourceConfig(BaseModel):
    path: Optional[str] = None
    filename_contains: Enum
    loadfile_call: Optional[str] = None
    date_format: Optional[str] = None
    dropna: Optional[List[str]] = None
    level: Optional[str] = None
    ingestionId: Optional[AssetTypes] = None
    alignment: Optional[Dict[str, Any]] = None

    # Validation de la valeur de loadfile_call
    @validator('loadfile_call')
    def validate_loadfile_call(cls, value):
        if not is_valid_combination(value):
            raise ValueError(f"Le format de loadfile_call '{value}' est invalide. Le format attendu est AssetTypes_FileTypes_loadfiles.")
        return value
    
    # Conversion/Validation de filename_contains en instance de FilenameContains
    @validator('filename_contains', pre=True)
    def validate_filename_contains(cls, value):
        if isinstance(value, str):
            try:
                return FilenameContains[value]
            except KeyError:
                raise ValueError(f"Valeur invalide pour filename_contains : '{value}'. Doit être une valeur de FilenameContains.")
        if isinstance(value, FilenameContains):
            return value
        raise ValueError(f"filename_contains doit être une valeur de FilenameContains, reçu {value}")

class AssetConfig(BaseModel):
    source: Dict[FileTypes, SourceConfig]

class ConfigSchema(BaseModel):
    assets: Dict[Union[Enum, str], Union[AssetConfig, Any]]  # Permet AssetConfig pour AssetTypes et Any pour d'autres clés (en dehors du scope de AssetTypes)

    @validator('assets', pre=True)
    def validate_assets(cls, assets):
        validated_assets = {}
        
        for key, value in assets.items():
            if key in AssetTypes.__members__:
                validated_assets[key] = AssetConfig(**value)
            else:
                validated_assets[key] = value
        
        return validated_assets


class FinanceSpecialFunctionScript(BaseModel):
    finance_special_function_script: Dict[str, str]

    @root_validator(pre=True)
    def validate_keys(cls, values):
        script_keys = values.get('finance_special_function_script', {}).keys()
        for key in script_keys:
            if not is_valid_combination(key):
                raise ValueError(f"Nom de clé invalide: {key}. Le format attendu est AssetTypes_FileTypes_loadfiles.")
        return values

class DatasetColumnConfig(BaseModel):
    columns: List[Any]
    dtypes: Dict[Any, str]

class FinanceDatasetSchema(RootModel):
    root: Dict[str, DatasetColumnConfig]

    @root_validator(pre=True)
    def validate_keys(cls, values):
        keys = values.keys()
        for key in keys:
            if not is_valid_combination(key):
                raise ValueError(f"Nom de clé invalide: {key}. Le format attendu est AssetTypes_FileTypes_loadfiles.")
        return values