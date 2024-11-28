import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Time': Column(pa.String, nullable=True, coerce=True),
    'Project': Column(pa.String, nullable=True, coerce=True),
    'Date': Column(pa.String, nullable=True, coerce=True),
    'Value': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
