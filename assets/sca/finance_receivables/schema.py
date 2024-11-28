import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'As of Date': Column(pa.String, nullable=True, coerce=True),
    'Doc Date': Column(pa.String, nullable=True, coerce=True),
    ' Due Date': Column(pa.String, nullable=True, coerce=True),
    'Short Name': Column(pa.String, nullable=True, coerce=True),
    'Customer No': Column(pa.String, nullable=True, coerce=True),
    ' Customer Name': Column(pa.String, nullable=True, coerce=True),
    'Document No': Column(pa.String, nullable=True, coerce=True),
    'Amount (USD)': Column(pa.Float, nullable=True, coerce=True),
    'Doc Type': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
