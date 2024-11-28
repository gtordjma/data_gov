import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Data de lançamento': Column(pa.String, nullable=True, coerce=True),
    'Data de vencimento': Column(pa.String, nullable=True, coerce=True),
    'Série': Column(pa.String, nullable=True, coerce=True),
    'Nº doc.': Column(pa.String, nullable=True, coerce=True),
    'Nº transação': Column(pa.Float, nullable=True, coerce=True),
    'Cta.contáb./cód.PN': Column(pa.String, nullable=True, coerce=True),
    'Observações': Column(pa.String, nullable=True, coerce=True),
    'Projeto': Column(pa.String, nullable=True, coerce=True),
    'Conta de contrapartida': Column(pa.String, nullable=True, coerce=True),
    'Nome conta contrap.': Column(pa.String, nullable=True, coerce=True),
    'Débito/crédito (MC)': Column(pa.String, nullable=True, coerce=True),
    'Saldo acumulado (MC)': Column(pa.Float, nullable=True, coerce=True),
    'Centro de Custo': Column(pa.String, nullable=True, coerce=True),
    'Nome do projeto': Column(pa.String, nullable=True, coerce=True),
    'Contrato guarda-chuva': Column(pa.Float, nullable=True, coerce=True),
    'Nº seq.': Column(pa.Float, nullable=True, coerce=True),
    'Nome da filial': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
