import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'MainAccount': Column(pa.String, nullable=True, coerce=True),
    'CostCentre': Column(pa.String, nullable=True, coerce=True),
    'ProfitCentre': Column(pa.Float, nullable=True, coerce=True),
    'Name': Column(pa.String, nullable=True, coerce=True),
    'Opening balance': Column(pa.String, nullable=True, coerce=True),
    'Debit': Column(pa.String, nullable=True, coerce=True),
    'Credit': Column(pa.String, nullable=True, coerce=True),
    'Closing transactions': Column(pa.Float, nullable=True, coerce=True),
    'Closing balance': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
