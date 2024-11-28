import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Local account number old': Column(pa.String, nullable=True, coerce=True),
    'Local account number': Column(pa.String, nullable=True, coerce=True),
    'Local account name': Column(pa.String, nullable=True, coerce=True),
    'Level 0': Column(pa.String, nullable=True, coerce=True),
    'Level 1': Column(pa.String, nullable=True, coerce=True),
    'Level 2': Column(pa.String, nullable=True, coerce=True),
    'Level 3': Column(pa.String, nullable=True, coerce=True),
    'Cockpit Code': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
