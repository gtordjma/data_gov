import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'asset': Column(pa.String, nullable=True, coerce=True),
    'airportIATACode': Column(pa.String, nullable=True, coerce=True),
    'accountId': Column(pa.String, nullable=True, coerce=True),
    'level0': Column(pa.String, nullable=True, coerce=True),
    'level1': Column(pa.String, nullable=True, coerce=True),
    'level2': Column(pa.String, nullable=True, coerce=True),
    'level3': Column(pa.String, nullable=True, coerce=True),
    'usecase': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
