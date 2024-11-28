import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Calendar Date': Column(pa.String, nullable=True, coerce=True),
    'Customer Account - Key': Column(pa.String, nullable=True, coerce=True),
    'Client Name': Column(pa.String, nullable=True, coerce=True),
    'Airline Code': Column(pa.String, nullable=True, coerce=True),
    'Client IATA code': Column(pa.String, nullable=True, coerce=True),
    'Client IACO Code': Column(pa.String, nullable=True, coerce=True),
    'Flight type - Key': Column(pa.Float, nullable=True, coerce=True),
    'Charge local ID ': Column(pa.String, nullable=True, coerce=True),
    'Invoicing lablel local': Column(pa.String, nullable=True, coerce=True),
    'Invoicing label Global': Column(pa.Float, nullable=True, coerce=True),
    'Amount': Column(pa.Float, nullable=True, coerce=True),
    'GL Account no.': Column(pa.String, nullable=True, coerce=True),
    'Instances': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
