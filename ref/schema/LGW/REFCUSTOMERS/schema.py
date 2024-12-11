import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=False, coerce=True),
    'Client category': Column(pa.String, nullable=True, coerce=True),
    'Client Id': Column(pa.Int, nullable=False, coerce=True),
    'Client Name': Column(pa.String, nullable=False, coerce=True),
    'Client Currency': Column(pa.String, nullable=False, coerce=True),
    'Client IATA Code': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)