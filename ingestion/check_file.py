from enum import Enum
import mimetypes
from typing import Optional

from fastapi import UploadFile

from data_gov.types import AssetTypes, FileTypes
from data_gov.error import DataGouvException

FilenameContains = Enum(
    'FilenameContains', 
    {
        name.replace('FINANCE_', '').upper(): name.replace('FINANCE_', '').upper()
        for name in FileTypes.__members__
    }
)

def validate_filename_type(filename: str) -> Enum:
    """
    Validates and returns the corresponding file type enum based on filename patterns.
    
    Args:
        filename (str): The input filename to validate (ex: DEPOSITS, CAPEX...)
        
    Returns:
        Enum: Matching FilenameContains enum value (ex: FilenameContains.DEPOSITS, FilenameContains.CAPEX)
        
    Raises:
        DataGouvException: If no valid file type is found in filename
        
    Description:
        Checks filename against predefined patterns to determine file type.
        Priority rules:
        1. Special CAPEX cases (CAPEX_B0, CAPEX_R1, etc.)
        2. Generic patterns (GL, SUPPLIER, etc.)
        3. Direct enum value matches
    """
    patterns = {
        "CAPEX_FORECAST": ["CAPEX_B0", "CAPEX_R1", "CAPEX_R2", "CAPEX_R3", "CPXFORECAST", "CAPEX_FORECAST"],
        "CAPEX": ["CAPEX"],
        "MAPPING_LOCAL": ["MAPPINGLOCAL"],
        "GENERAL_LEDGER": ["GL"],
        "SUPPLIER_OPEX": ["SUPPLIER"],
        "CUSTOMER_REVENUES": ["CUSTOMER"]
    }
    
    # Check patterns first
    for enum_key, pattern_list in patterns.items():
        if any(pattern in filename for pattern in pattern_list):
            return FilenameContains[enum_key]
    
    # Check direct enum values
    for enum_value in FilenameContains:
        if enum_value.value in filename:
            return enum_value
            
    raise DataGouvException(
        title="Validate Filename Type",
        description="Validate Filename Type Error: No valid type found in filename."
    )
    
def validate_asset(filename: str) -> Optional[AssetTypes]:
    for valeur in AssetTypes:
            if valeur.value in filename:
                return valeur
    return None

def validate_mime_type(file: UploadFile):
    mime_type, _ = mimetypes.guess_type(file.filename)
    if mime_type is None:
        mime_type = "application/octet-stream" 
        
    if mime_type == "text/csv":
        return "csv"
    elif mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return "xlsx"
    else:
        raise DataGouvException(
            title="Validate Mime Type",
            description="Validate Mime Type Error: Mime not supported, only csv or xlsx files accepted."
        )