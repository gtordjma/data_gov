import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Level 4 - Local account code': Column(pa.Float, nullable=True, coerce=True),
    'Level 4 - Local account name': Column(pa.String, nullable=True, coerce=True),
    'Level 3': Column(pa.String, nullable=True, coerce=True),
    'Level 2': Column(pa.String, nullable=True, coerce=True),
    'Level 1': Column(pa.String, nullable=True, coerce=True),
    'Level 0': Column(pa.String, nullable=True, coerce=True),
    'Sign': Column(pa.Float, nullable=True, coerce=True),
    'Cockpit Code': Column(pa.String, nullable=True, coerce=True),
    'Level 0 order': Column(pa.Float, nullable=True, coerce=True),
    'Level 1 order': Column(pa.Float, nullable=True, coerce=True),
    'Level 2 order': Column(pa.Float, nullable=True, coerce=True),
    'Level 3 order': Column(pa.Float, nullable=True, coerce=True),
    'Level 4 order': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)