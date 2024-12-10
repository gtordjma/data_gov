import pandera as pa
from pandera import Column, DataFrameSchema,Index

schema = DataFrameSchema(
    columns={
        'Clients': Column(pa.Int, nullable=False, coerce=True),
        'Name': Column(pa.String, nullable=False, coerce=True),
        'IATA kod': Column(pa.String, nullable=False, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)

