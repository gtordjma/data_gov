import pandera as pa
from pandera import Column, DataFrameSchema,Index

schema = DataFrameSchema({
    'Code client': Column(pa.String, nullable=False, coerce=True),
    'Nom client': Column(pa.String, nullable=False, coerce=True),
    'Pays': Column(pa.String, nullable=False, coerce=True),
    'Code IATA': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)