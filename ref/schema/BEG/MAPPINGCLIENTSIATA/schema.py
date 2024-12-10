import pandera as pa
from pandera import Column, DataFrameSchema, Index

schema = DataFrameSchema(
    columns={
        'clientIATACode': Column(pa.String, nullable=False, coerce=True),
        'clientSupplId': Column(pa.Int, nullable=False, coerce=True),
        'clientSupplName': Column(pa.String, nullable=False, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)

