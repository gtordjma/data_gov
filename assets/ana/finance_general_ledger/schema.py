import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Nº documento': Column(pa.Float, nullable=True, coerce=True),
    'Linha de lançamento': Column(pa.Float, nullable=True, coerce=True),
    'Data de entrada': Column(pa.String, nullable=True, coerce=True),
    'Período contábil': Column(pa.Float, nullable=True, coerce=True),
    'Data de lançamento': Column(pa.String, nullable=True, coerce=True),
    'Centro de lucro': Column(pa.String, nullable=True, coerce=True),
    'Divisão': Column(pa.String, nullable=True, coerce=True),
    'Nº conta': Column(pa.String, nullable=True, coerce=True),
    'Denominação': Column(pa.String, nullable=True, coerce=True),
    'em moeda interna do centro de lucro': Column(pa.String, nullable=True, coerce=True),
    'Código moeda MI CtrLuc.': Column(pa.String, nullable=True, coerce=True),
    'Cliente': Column(pa.Float, nullable=True, coerce=True),
    'Fornecedor': Column(pa.Float, nullable=True, coerce=True),
    'Client description': Column(pa.String, nullable=True, coerce=True),
    'Supplier description': Column(pa.String, nullable=True, coerce=True),
    'IATA Code': Column(pa.String, nullable=True, coerce=True),
    'Unique Code': Column(pa.String, nullable=True, coerce=True),
    'Asset': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
