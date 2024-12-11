import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Projeto': Column(pa.String, nullable=False, coerce=True),
    'Name of project': Column(pa.String, nullable=False, coerce=True),
    'Cost Center': Column(pa.String, nullable=False, coerce=True),
    'Type': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)