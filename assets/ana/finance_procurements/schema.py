import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Supplier Id': Column(pa.Float, nullable=True, coerce=True),
    'Supplier name': Column(pa.String, nullable=True, coerce=True),
    'Account no.': Column(pa.Float, nullable=True, coerce=True),
    'Document no.': Column(pa.Float, nullable=True, coerce=True),
    'Emission date': Column(pa.String, nullable=True, coerce=True),
    'due date': Column(pa.String, nullable=True, coerce=True),
    'Amount': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
