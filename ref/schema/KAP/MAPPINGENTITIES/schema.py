import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Department': Column(pa.String, nullable=False, coerce=True),
    'Entité': Column(pa.String, nullable=False, coerce=True),
    'Descriptif': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)