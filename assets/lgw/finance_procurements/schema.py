import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Supplier Id': Column(pa.Float, nullable=True, coerce=True),
    'Document no': Column(pa.Float, nullable=True, coerce=True),
    'Accounting date': Column(pa.String, nullable=True, coerce=True),
    'Net due date': Column(pa.String, nullable=True, coerce=True),
    'Amount': Column(pa.Float, nullable=True, coerce=True),
    'Currency': Column(pa.String, nullable=True, coerce=True),
    'extraction date': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
