import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    '665000': Column(pa.String, nullable=True, coerce=True),
    'ESCOMPTES ACCORDES': Column(pa.String, nullable=True, coerce=True),
    '665000-ESCOMPTES ACCORDES': Column(pa.String, nullable=True, coerce=True),
    'Autres revenus': Column(pa.String, nullable=True, coerce=True),
    'Non-Aero Revenues': Column(pa.String, nullable=True, coerce=True),
    'Revenues': Column(pa.String, nullable=True, coerce=True),
    '130400': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
