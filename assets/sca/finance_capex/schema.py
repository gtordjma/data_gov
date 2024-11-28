import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Account Number                                        ': Column(pa.String, nullable=True, coerce=True),
    'Description                                                         ': Column(pa.String, nullable=True, coerce=True),
    'Debits': Column(pa.Float, nullable=True, coerce=True),
    'Credits': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
