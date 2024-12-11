import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'BU Code': Column(pa.String, nullable=False, coerce=True),
    'Cost Center Code': Column(pa.String, nullable=False, coerce=True),
    'Cost Center description': Column(pa.String, nullable=False, coerce=True),
    'BU': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)