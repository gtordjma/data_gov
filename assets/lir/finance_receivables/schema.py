import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Número/Tipo de Documento': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 1': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 2': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 3': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 4': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 5': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 6': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 7': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 8': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 9': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 10': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 11': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 12': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 13': Column(pa.String, nullable=True, coerce=True),
    'Fecha Doc.': Column(pa.DateTime, nullable=True, coerce=True),
    'Plazo o N° de Cheque/Recibo': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 16': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 17': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 18': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 19': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 20': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 21': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 22': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 23': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 24': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 25': Column(pa.Float, nullable=True, coerce=True),
    'Actual': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 27': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 28': Column(pa.Float, nullable=True, coerce=True),
    'Días': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 30': Column(pa.Float, nullable=True, coerce=True),
    'Días.1': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 32': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 33': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 34': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 35': Column(pa.Float, nullable=True, coerce=True),
    'Días.2': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 37': Column(pa.Float, nullable=True, coerce=True),
    'Días.3': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 39': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 40': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 41': Column(pa.Float, nullable=True, coerce=True),
    'Total': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
