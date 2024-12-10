import pandera as pa
from pandera import Column, DataFrameSchema, Index

schema = DataFrameSchema(
    columns={
        'Section': Column(pa.Int, nullable=False, coerce=True),
        'Code IATA Airport': Column(pa.String, nullable=False, coerce=True),
        'Airport': Column(pa.String, nullable=False, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)