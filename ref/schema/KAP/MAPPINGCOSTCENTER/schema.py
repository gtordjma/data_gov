import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'PJ Code': Column(pa.String, nullable=False, coerce=True),
    'Cost Center': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)