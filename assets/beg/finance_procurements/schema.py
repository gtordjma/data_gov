import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Invoice/Reference': Column(pa.String, nullable=True, coerce=True),
    'Date of invoice': Column(pa.DateTime, nullable=True, coerce=True),
    'Due dates': Column(pa.DateTime, nullable=True, coerce=True),
    'Amount': Column(pa.Float, nullable=True, coerce=True),
    'Currency': Column(pa.String, nullable=True, coerce=True),
    'Supplier code': Column(pa.Float, nullable=True, coerce=True),
    'Supplier name': Column(pa.String, nullable=True, coerce=True),
    'GL local account': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
