import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'BU': Column(pa.String, nullable=True, coerce=True),
    'Airport IATA Code': Column(pa.String, nullable=True, coerce=True),
    'Currency': Column(pa.String, nullable=True, coerce=True),
    'Updated Date of the report': Column(pa.DateTime, nullable=True, coerce=True),
    'Termination date of the Guarantee': Column(pa.DateTime, nullable=True, coerce=True),
    'Accounting Client code': Column(pa.String, nullable=True, coerce=True),
    'IATA Code': Column(pa.String, nullable=True, coerce=True),
    'Client name': Column(pa.String, nullable=True, coerce=True),
    'Guarantee amount': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
