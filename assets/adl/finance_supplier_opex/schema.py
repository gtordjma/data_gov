import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'TYP': Column(pa.String, nullable=True, coerce=True),
    'NUM': Column(pa.String, nullable=True, coerce=True),
    'LIN': Column(pa.Float, nullable=True, coerce=True),
    'FCYLIN': Column(pa.String, nullable=True, coerce=True),
    'ACCDAT': Column(pa.String, nullable=True, coerce=True),
    'ACC': Column(pa.Float, nullable=True, coerce=True),
    'DES compte': Column(pa.String, nullable=True, coerce=True),
    'AMTCUR': Column(pa.String, nullable=True, coerce=True),
    'CUR': Column(pa.String, nullable=True, coerce=True),
    'OFFACC': Column(pa.String, nullable=True, coerce=True),
    'DES écriture': Column(pa.String, nullable=True, coerce=True),
    'SNS': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
