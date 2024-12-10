import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'CC': Column(pa.String, nullable=False, coerce=True),
    'Descrição': Column(pa.String, nullable=False, coerce=True),
    'Airport': Column(pa.String, nullable=False, coerce=True),
    'Airport + description': Column(pa.String, nullable=False, coerce=True),
    'Decription 2': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)