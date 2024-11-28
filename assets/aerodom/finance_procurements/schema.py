import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Fecha': Column(pa.String, nullable=True, coerce=True),
    'Tipo': Column(pa.String, nullable=True, coerce=True),
    'Nº': Column(pa.String, nullable=True, coerce=True),
    'Fecha.1': Column(pa.String, nullable=True, coerce=True),
    'Importe': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 5': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 6': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 7': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 8': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 9': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 10': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 11': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 12': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 13': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 14': Column(pa.Float, nullable=True, coerce=True),
    'Más de': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 16': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
