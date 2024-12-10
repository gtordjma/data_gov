import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'BPSNUM': Column(pa.String, nullable=False, coerce=True),
    'BPSNAM': Column(pa.String, nullable=False, coerce=True),
    'BPSSHO': Column(pa.String, nullable=False, coerce=True),
    'BSGCOD': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)