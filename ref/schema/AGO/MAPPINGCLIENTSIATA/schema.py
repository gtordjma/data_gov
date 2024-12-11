import pandera as pa
from pandera import Column, DataFrameSchema, Index

schema = DataFrameSchema(
    columns={
        'Client IATA code': Column(pa.String, nullable=False, coerce=True),
        'Client ID': Column(pa.Int, nullable=False, coerce=True),
        'Client Name': Column(pa.String, nullable=False, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)