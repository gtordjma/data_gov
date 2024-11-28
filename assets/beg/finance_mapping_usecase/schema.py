import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Account Number': Column(pa.String, nullable=True, coerce=True),
    'Account Name': Column(pa.String, nullable=True, coerce=True),
    'Cockpit account': Column(pa.String, nullable=True, coerce=True),
    'Level 0': Column(pa.String, nullable=True, coerce=True),
    'Level 1': Column(pa.String, nullable=True, coerce=True),
    'Level 2': Column(pa.String, nullable=True, coerce=True),
    'Level 3': Column(pa.String, nullable=True, coerce=True),
    'Level 0 code': Column(pa.Float, nullable=True, coerce=True),
    'Level 1 code': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
