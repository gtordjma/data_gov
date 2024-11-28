import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Unnamed: 0': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 1': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 2': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 3': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 4': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 5': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 6': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 7': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 8': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 9': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 10': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 11': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 12': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 13': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 14': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 15': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 16': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 17': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 18': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
