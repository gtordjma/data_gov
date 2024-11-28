import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Affiliated department Name': Column(pa.String, nullable=True, coerce=True),
    'Unique project Id': Column(pa.String, nullable=True, coerce=True),
    'Unique Project Name': Column(pa.String, nullable=True, coerce=True),
    'Project Category 1': Column(pa.String, nullable=True, coerce=True),
    'Project Category 2': Column(pa.String, nullable=True, coerce=True),
    'Project Category 3': Column(pa.Float, nullable=True, coerce=True),
    'Extraction Date': Column(pa.String, nullable=True, coerce=True),
    'Total project amount planned on CY': Column(pa.Float, nullable=True, coerce=True),
    'Total project amount planned': Column(pa.Float, nullable=True, coerce=True),
    'Total project amount spent on CY': Column(pa.Float, nullable=True, coerce=True),
    'Total project amount spent': Column(pa.Float, nullable=True, coerce=True),
    'Anticipated Final Cost': Column(pa.Float, nullable=True, coerce=True),
    'Closed off': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
