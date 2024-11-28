import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'ACCTID': Column(pa.String, nullable=True, coerce=True),
    'FSCSYR': Column(pa.Float, nullable=True, coerce=True),
    'FSCSDSG': Column(pa.Float, nullable=True, coerce=True),
    'FSCSCURN': Column(pa.String, nullable=True, coerce=True),
    'CURNTYPE': Column(pa.String, nullable=True, coerce=True),
    'NETPERD1': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD2': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD3': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD4': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD5': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD6': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD7': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD8': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD9': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD10': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD11': Column(pa.Float, nullable=True, coerce=True),
    'NETPERD12': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
