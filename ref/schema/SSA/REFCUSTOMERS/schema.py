import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Code': Column(pa.Int, nullable=False, coerce=True),
    'Airline': Column(pa.String, nullable=False, coerce=True),
    'IATA_Code': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)