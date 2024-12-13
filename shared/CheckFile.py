from fastapi import UploadFile

from .DataGouvException import DataGouvException


def validate_file_extension(file: UploadFile):
    file_extension = file.filename.split('.')[-1].lower() if '.' in file.filename else None
    accepted_extensions = ["csv", "xlsx", "xls", "xlsm", ]
    if file_extension in accepted_extensions:
        return file_extension
    else:
        raise DataGouvException(
            title="Validate File Extension",
            description=f"Validate File Extension Error: Extension not supported ({file_extension}), only csv, xlsx, xls, or xlsm files accepted."
        )
