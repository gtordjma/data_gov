import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Número': Column(pa.Int, nullable=False, coerce=True),
    'Nome da filial': Column(pa.String, nullable=False, coerce=True),
    'Nome fantasia': Column(pa.String, nullable=False, coerce=True),
    'CNPJ': Column(pa.String, nullable=False, coerce=True),
    'Município': Column(pa.String, nullable=False, coerce=True),
    'Estado': Column(pa.String, nullable=False, coerce=True),
    'País': Column(pa.String, nullable=False, coerce=True),
    'Airport IATA Code': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)