import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Invoice/Reference': Column(pa.String, nullable=True, coerce=True),
    'Date of invoice': Column(pa.DateTime, nullable=True, coerce=True),
    'Due dates': Column(pa.DateTime, nullable=True, coerce=True),
    'Amount': Column(pa.Float, nullable=True, coerce=True),
    'Currency': Column(pa.String, nullable=True, coerce=True),
    'Customer code': Column(pa.Float, nullable=True, coerce=True),
    'Customer name': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
