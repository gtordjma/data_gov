import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Client Id': Column(pa.Float, nullable=True, coerce=True),
    'Document no': Column(pa.Float, nullable=True, coerce=True),
    'Extraction date': Column(pa.String, nullable=True, coerce=True),
    'Accounting date': Column(pa.String, nullable=True, coerce=True),
    'Expiration date': Column(pa.String, nullable=True, coerce=True),
    'Amount due': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
