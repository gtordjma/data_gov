import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Filial': Column(pa.String, nullable=True, coerce=True),
    'Código da conta': Column(pa.String, nullable=True, coerce=True),
    'Nome da conta': Column(pa.String, nullable=True, coerce=True),
    'Detalhes de linha': Column(pa.String, nullable=True, coerce=True),
    'Data de lançamento': Column(pa.String, nullable=True, coerce=True),
    'Valor CC': Column(pa.Float, nullable=True, coerce=True),
    'Código do centro': Column(pa.String, nullable=True, coerce=True),
    'EBITDA': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
