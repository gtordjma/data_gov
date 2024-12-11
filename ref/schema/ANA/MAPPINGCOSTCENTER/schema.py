import pandera as pa
from pandera import Column, DataFrameSchema, Index

schema = DataFrameSchema(
    columns={
        'Profit Center': Column(pa.String, nullable=False, coerce=True),
        'Profit center description': Column(pa.String, nullable=False, coerce=True),
        'Airport / Dep.': Column(pa.String, nullable=False, coerce=True),
        'Airport / Dep. Description': Column(pa.String, nullable=False, coerce=True),
        'Project Manager': Column(pa.String, nullable=False, coerce=True),
        'Airport / Dep #': Column(pa.String, nullable=False, coerce=True),
        'IATA Code': Column(pa.String, nullable=False, coerce=True),
        'Local': Column(pa.String, nullable=False, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)

