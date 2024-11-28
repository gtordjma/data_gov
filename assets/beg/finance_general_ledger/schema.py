import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'accountingDate': Column(pa.DateTime, nullable=True, coerce=True),
    'accountId': Column(pa.Float, nullable=True, coerce=True),
    'costCode': Column(pa.String, nullable=True, coerce=True),
    'costName': Column(pa.String, nullable=True, coerce=True),
    'amount': Column(pa.Float, nullable=True, coerce=True),
    'currency': Column(pa.String, nullable=True, coerce=True),
    'documentID': Column(pa.Float, nullable=True, coerce=True),
    'clientIATACode': Column(pa.String, nullable=True, coerce=True),
    'clientSupplId': Column(pa.Float, nullable=True, coerce=True),
    'clientSupplName': Column(pa.String, nullable=True, coerce=True),
    'airportIATACode': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
