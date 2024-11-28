import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Updated Date of the report': Column(pa.DateTime, nullable=True, coerce=True),
    'Accounting Client code': Column(pa.String, nullable=True, coerce=True),
    'Client name': Column(pa.String, nullable=True, coerce=True),
    'Client IATA Code': Column(pa.String, nullable=True, coerce=True),
    'Currency': Column(pa.String, nullable=True, coerce=True),
    'Guarantee amount': Column(pa.Float, nullable=True, coerce=True),
    'Termination date of the Guarantee': Column(pa.String, nullable=True, coerce=True),
    'BU': Column(pa.String, nullable=True, coerce=True),
    'Comments': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)