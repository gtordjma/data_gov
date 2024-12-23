import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Filial': Column(pa.Float, nullable=True, coerce=True),
    'ID Origem': Column(pa.Float, nullable=True, coerce=True),
    'Nro Origem': Column(pa.String, nullable=True, coerce=True),
    'Codigo Cli/For': Column(pa.String, nullable=True, coerce=True),
    'Nome Cli/For': Column(pa.String, nullable=True, coerce=True),
    'Nº da transação': Column(pa.Float, nullable=True, coerce=True),
    'Doc Origem': Column(pa.String, nullable=True, coerce=True),
    'Nº origem': Column(pa.Float, nullable=True, coerce=True),
    'Data de lançamento': Column(pa.String, nullable=True, coerce=True),
    'Observações': Column(pa.String, nullable=True, coerce=True),
    'Referência 1': Column(pa.Float, nullable=True, coerce=True),
    'Referência 2': Column(pa.Float, nullable=True, coerce=True),
    'Total em moeda do sistema': Column(pa.Float, nullable=True, coerce=True),
    'Código da transação': Column(pa.Float, nullable=True, coerce=True),
    'Código do projeto': Column(pa.Float, nullable=True, coerce=True),
    'Data de vencimento': Column(pa.String, nullable=True, coerce=True),
    'Data do documento': Column(pa.String, nullable=True, coerce=True),
    'Detalhes de linha': Column(pa.String, nullable=True, coerce=True),
    'Código da conta': Column(pa.String, nullable=True, coerce=True),
    'Nome da conta': Column(pa.String, nullable=True, coerce=True),
    'Conta de contrapartida': Column(pa.String, nullable=True, coerce=True),
    'Nome da conta.1': Column(pa.String, nullable=True, coerce=True),
    'Valor de Débito': Column(pa.Float, nullable=True, coerce=True),
    'Valor de Crédito': Column(pa.Float, nullable=True, coerce=True),
    'Código do projeto.1': Column(pa.String, nullable=True, coerce=True),
    'Saldo': Column(pa.Float, nullable=True, coerce=True),
    'PN/código conta': Column(pa.String, nullable=True, coerce=True),
    'Regra distribuição': Column(pa.String, nullable=True, coerce=True),
    'Código do centro': Column(pa.String, nullable=True, coerce=True),
    'Total no centro': Column(pa.Float, nullable=True, coerce=True),
    'Valor CC': Column(pa.Float, nullable=True, coerce=True),
    'Itens': Column(pa.String, nullable=True, coerce=True),
    'NroContrato': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
