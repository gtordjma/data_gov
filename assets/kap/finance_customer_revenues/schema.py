import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'airportIATACode': Column(pa.String, nullable=True, coerce=True),
    'accountingDate': Column(pa.String, nullable=True, coerce=True),
    'accountId': Column(pa.Float, nullable=True, coerce=True),
    'amountValue': Column(pa.Float, nullable=True, coerce=True),
    'currencyLocal': Column(pa.String, nullable=True, coerce=True),
    'clientIATACode': Column(pa.String, nullable=True, coerce=True),
    'clientId': Column(pa.Float, nullable=True, coerce=True),
    'clientName': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
