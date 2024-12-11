import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Client N°': Column(pa.String, nullable=False, coerce=True),
    'Name': Column(pa.String, nullable=False, coerce=True),
    'IATA Code': Column(pa.String, nullable=True, coerce=True),  # Nullable car certaines valeurs peuvent être manquantes
},
    strict=True,
    coerce=True,
)