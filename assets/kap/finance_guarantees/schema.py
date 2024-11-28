import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'airportIATACode': Column(pa.String, nullable=True, coerce=True),
    'extractDate': Column(pa.DateTime, nullable=True, coerce=True),
    'customerId': Column(pa.Float, nullable=True, coerce=True),
    'paymentDate': Column(pa.DateTime, nullable=True, coerce=True),
    'expirationDate': Column(pa.DateTime, nullable=True, coerce=True),
    'amountValue': Column(pa.Float, nullable=True, coerce=True),
    'currencyLocal': Column(pa.String, nullable=True, coerce=True),
    'Customer IATA code': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
