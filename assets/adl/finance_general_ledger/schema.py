import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Unnamed: 0': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 1': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 2': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 3': Column(pa.String, nullable=True, coerce=True),
    'JAN': Column(pa.String, nullable=True, coerce=True),
    'FEV': Column(pa.String, nullable=True, coerce=True),
    'MAR': Column(pa.String, nullable=True, coerce=True),
    'AVR': Column(pa.String, nullable=True, coerce=True),
    'MAI': Column(pa.String, nullable=True, coerce=True),
    'JUN': Column(pa.String, nullable=True, coerce=True),
    'JUL': Column(pa.String, nullable=True, coerce=True),
    'AOU': Column(pa.String, nullable=True, coerce=True),
    'SEP': Column(pa.String, nullable=True, coerce=True),
    'OCT': Column(pa.String, nullable=True, coerce=True),
    'NOV': Column(pa.String, nullable=True, coerce=True),
    'DEC': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
