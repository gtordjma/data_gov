import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Unnamed: 0': Column(pa.String, nullable=True, coerce=True),
    'CICA': Column(pa.String, nullable=True, coerce=True),
    'Level 0': Column(pa.String, nullable=True, coerce=True),
    'Level 1': Column(pa.String, nullable=True, coerce=True),
    'Level 2': Column(pa.String, nullable=True, coerce=True),
    'Level 3': Column(pa.String, nullable=True, coerce=True),
    'Account Local': Column(pa.String, nullable=True, coerce=True),
    'Account Name - ES (OMA)': Column(pa.String, nullable=True, coerce=True),
    'Account Name - EN': Column(pa.String, nullable=True, coerce=True),
    'Account - Cockpit': Column(pa.String, nullable=True, coerce=True),
    'Activity - Cockpit': Column(pa.String, nullable=True, coerce=True),
    'Account - Cockpit.1': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
