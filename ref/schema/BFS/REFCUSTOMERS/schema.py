import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'textbox143': Column(pa.Int, nullable=False, coerce=True),  # Code client (numérique)
    'textbox134': Column(pa.String, nullable=False, coerce=True),  # Nom client (chaîne de caractères)
    'IATA code': Column(pa.String, nullable=True, coerce=True),    # Code IATA (chaîne de caractères)
},
    strict=True,
    coerce=True,
)