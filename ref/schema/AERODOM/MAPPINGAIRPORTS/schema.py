import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Codes internes (capex)': Column(pa.String, nullable=False, coerce=True),
    'IATA': Column(pa.String, nullable=False, coerce=True),
    'Nom': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)