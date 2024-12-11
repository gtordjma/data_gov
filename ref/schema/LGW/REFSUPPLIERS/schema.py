import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=False, coerce=True),
    'Supplier category': Column(pa.String, nullable=True, coerce=True),
    'Supplier group category': Column(pa.String, nullable=True, coerce=True),
    'Supplier Id': Column(pa.Int, nullable=False, coerce=True),
    'Supplier group Id': Column(pa.String, nullable=True, coerce=True),
    'Supplier Name': Column(pa.String, nullable=False, coerce=True),
    'Supplier group name VINCI': Column(pa.String, nullable=True, coerce=True),
    'Supplier Currency': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)