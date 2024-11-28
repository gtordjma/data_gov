import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Local Account': Column(pa.Float, nullable=True, coerce=True),
    'Coriport Account - Level 4': Column(pa.String, nullable=True, coerce=True),
    'Local Account description': Column(pa.String, nullable=True, coerce=True),
    'Level 0': Column(pa.String, nullable=True, coerce=True),
    'Level 1': Column(pa.String, nullable=True, coerce=True),
    'Level 2': Column(pa.String, nullable=True, coerce=True),
    'Level 3': Column(pa.String, nullable=True, coerce=True),
    'Cockpit account': Column(pa.String, nullable=True, coerce=True),
    'Cockpit Description': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
