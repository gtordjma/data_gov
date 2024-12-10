import pandera as pa
from pandera import Column, DataFrameSchema, Index

schema = DataFrameSchema(
    columns={
        'Code Area': Column(pa.String, nullable=False, coerce=True),
        'Department Name SP': Column(pa.String, nullable=False, coerce=True),
        'Department Name EN': Column(pa.String, nullable=False, coerce=True),
        'Present in capex file (Y/N)': Column(pa.String, nullable=True, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)