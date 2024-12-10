import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'BPCNUM': Column(pa.String, nullable=False, coerce=True),
    'BPCNAM': Column(pa.String, nullable=False, coerce=True),
    'BPCSHO': Column(pa.String, nullable=False, coerce=True),
    'BCGCOD': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)