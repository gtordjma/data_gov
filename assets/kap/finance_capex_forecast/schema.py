import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Unnamed: 1': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 2': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 3': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 4': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 5': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 6': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 7': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 8': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 9': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 10': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 11': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 12': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 13': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 14': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 15': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 16': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 17': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 18': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 19': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 20': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 21': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 22': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 23': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 24': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 25': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 26': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 27': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 28': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 29': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 30': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 31': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 32': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 33': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 34': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 35': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 36': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 37': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 38': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 39': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 40': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 41': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 42': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 43': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 44': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 45': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 46': Column(pa.Float, nullable=True, coerce=True),
    'Unnamed: 47': Column(pa.Float, nullable=True, coerce=True),
    'Apr Actual': Column(pa.Float, nullable=True, coerce=True),
    'May Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Jun Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Jul Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Aug Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Sep Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Oct Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Nov Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Dec Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Jan Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Feb Estimate': Column(pa.Float, nullable=True, coerce=True),
    'Mar Estimate': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)