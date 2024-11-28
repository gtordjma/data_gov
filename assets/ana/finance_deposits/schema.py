import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Client Id': Column(pa.Float, nullable=True, coerce=True),
    'Name': Column(pa.String, nullable=True, coerce=True),
    'IATA Code': Column(pa.String, nullable=True, coerce=True),
    'Document no.': Column(pa.String, nullable=True, coerce=True),
    'Date d'extraction': Column(pa.String, nullable=True, coerce=True),
    'Accounting Date': Column(pa.String, nullable=True, coerce=True),
    'Expiration Date': Column(pa.String, nullable=True, coerce=True),
    'Amount due': Column(pa.String, nullable=True, coerce=True),
    'Deposit Amount': Column(pa.String, nullable=True, coerce=True),
    'date of the guarantee': Column(pa.String, nullable=True, coerce=True),
    'Guaranties amount': Column(pa.String, nullable=True, coerce=True),
    'date of the deposit': Column(pa.String, nullable=True, coerce=True),
    'Expiration Date.1': Column(pa.String, nullable=True, coerce=True),
    'Provisions amount': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
