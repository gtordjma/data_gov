import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Cost Center': Column(pa.String, nullable=False, coerce=True),  # Cost Center comme chaîne de caractères
    'Department': Column(pa.String, nullable=False, coerce=True),  # Department comme chaîne de caractères
},
    strict=True,
    coerce=True,
)