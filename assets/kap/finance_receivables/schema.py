import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'airportIATACode': Column(pa.String, nullable=True, coerce=True),
    'extractDate': Column(pa.DateTime, nullable=True, coerce=True),
    'accountingDate': Column(pa.DateTime, nullable=True, coerce=True),
    'dueDate': Column(pa.DateTime, nullable=True, coerce=True),
    'clientIATACode': Column(pa.String, nullable=True, coerce=True),
    'customerId': Column(pa.Float, nullable=True, coerce=True),
    'customerName': Column(pa.String, nullable=True, coerce=True),
    'documentId': Column(pa.String, nullable=True, coerce=True),
    'amountValue': Column(pa.Float, nullable=True, coerce=True),
    'currencyLocal': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
