import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Número': Column(pa.String, nullable=False, coerce=True),  # Utilisation de pa.String car les numéros sont sous forme de chaîne de caractères
    'Español': Column(pa.String, nullable=False, coerce=True),
    'Inglés': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)

