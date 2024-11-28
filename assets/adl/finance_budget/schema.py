import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Unnamed: 0': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 1': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 2': Column(pa.String, nullable=True, coerce=True),
    'Janvier': Column(pa.Float, nullable=True, coerce=True),
    'Février': Column(pa.Float, nullable=True, coerce=True),
    'Mars': Column(pa.Float, nullable=True, coerce=True),
    'Avril': Column(pa.Float, nullable=True, coerce=True),
    'Mai': Column(pa.Float, nullable=True, coerce=True),
    'Juin': Column(pa.Float, nullable=True, coerce=True),
    'Juillet': Column(pa.Float, nullable=True, coerce=True),
    'Aout': Column(pa.Float, nullable=True, coerce=True),
    'Septembre': Column(pa.Float, nullable=True, coerce=True),
    'Octobre': Column(pa.Float, nullable=True, coerce=True),
    'Novembre': Column(pa.Float, nullable=True, coerce=True),
    'Décembre': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
