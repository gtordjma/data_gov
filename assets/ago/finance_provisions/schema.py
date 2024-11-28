import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Section': Column(pa.String, nullable=True, coerce=True),
    'N° compte': Column(pa.String, nullable=True, coerce=True),
    'Nom du client': Column(pa.String, nullable=True, coerce=True),
    'PROVISIONS CLOTURE': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
