import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Unnamed: 0': Column(pa.Float, nullable=True, coerce=True),
    'Updated Date of the report': Column(pa.DateTime, nullable=True, coerce=True),
    'Termination date of the Guarantee': Column(pa.String, nullable=True, coerce=True),
    'Client code': Column(pa.Float, nullable=True, coerce=True),
    'Client name': Column(pa.String, nullable=True, coerce=True),
    'Currency': Column(pa.String, nullable=True, coerce=True),
    'Guarantee amount': Column(pa.Float, nullable=True, coerce=True),
    'Document Type': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 8': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
