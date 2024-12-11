import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'No. SAP': Column(pa.String, nullable=False, coerce=True),  # Numéros SAP comme chaînes de caractères
    'Cliente': Column(pa.String, nullable=False, coerce=True),  # Noms de clients comme chaînes de caractères
    'CÓDIGO IATA': Column(pa.String, nullable=False, coerce=True),  # Codes IATA comme chaînes de caractères
},
    strict=True,
    coerce=True,
)