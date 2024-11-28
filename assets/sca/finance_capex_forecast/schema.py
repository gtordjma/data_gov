import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Account Number': Column(pa.String, nullable=True, coerce=True),
    'Description': Column(pa.String, nullable=True, coerce=True),
    'Extract Date': Column(pa.DateTime, nullable=True, coerce=True),
    'N-1': Column(pa.Float, nullable=True, coerce=True),
    'Jan': Column(pa.Float, nullable=True, coerce=True),
    'Feb': Column(pa.Float, nullable=True, coerce=True),
    'Mar': Column(pa.Float, nullable=True, coerce=True),
    'Apr': Column(pa.Float, nullable=True, coerce=True),
    'May': Column(pa.Float, nullable=True, coerce=True),
    'Jun': Column(pa.Float, nullable=True, coerce=True),
    'Jul': Column(pa.Float, nullable=True, coerce=True),
    'Aug': Column(pa.Float, nullable=True, coerce=True),
    'Sep': Column(pa.Float, nullable=True, coerce=True),
    'Oct': Column(pa.Float, nullable=True, coerce=True),
    'Nov': Column(pa.Float, nullable=True, coerce=True),
    'Dec': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
