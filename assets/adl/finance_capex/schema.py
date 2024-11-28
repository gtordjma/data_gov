import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    '0': Column(pa.String, nullable=True, coerce=True),
    '1': Column(pa.String, nullable=True, coerce=True),
    '2': Column(pa.String, nullable=True, coerce=True),
    '3': Column(pa.String, nullable=True, coerce=True),
    '4': Column(pa.String, nullable=True, coerce=True),
    '5': Column(pa.Float, nullable=True, coerce=True),
    '6': Column(pa.Float, nullable=True, coerce=True),
    '7': Column(pa.Float, nullable=True, coerce=True),
    '8': Column(pa.Float, nullable=True, coerce=True),
    '9': Column(pa.Float, nullable=True, coerce=True),
    '10': Column(pa.Float, nullable=True, coerce=True),
    '11': Column(pa.Float, nullable=True, coerce=True),
    '12': Column(pa.Float, nullable=True, coerce=True),
    '13': Column(pa.Float, nullable=True, coerce=True),
    '14': Column(pa.Float, nullable=True, coerce=True),
    '15': Column(pa.Float, nullable=True, coerce=True),
    '16': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
