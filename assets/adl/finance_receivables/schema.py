import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'TYP': Column(pa.String, nullable=True, coerce=True),
    'NUM': Column(pa.String, nullable=True, coerce=True),
    'LIG': Column(pa.Float, nullable=True, coerce=True),
    'CPY': Column(pa.String, nullable=True, coerce=True),
    'FCY': Column(pa.String, nullable=True, coerce=True),
    'SAC': Column(pa.String, nullable=True, coerce=True),
    'BPR': Column(pa.String, nullable=True, coerce=True),
    'BPRTYP': Column(pa.String, nullable=True, coerce=True),
    'BPRPAY': Column(pa.String, nullable=True, coerce=True),
    'DUDDAT': Column(pa.String, nullable=True, coerce=True),
    'PAM': Column(pa.String, nullable=True, coerce=True),
    'PAMTYP': Column(pa.String, nullable=True, coerce=True),
    'SNS': Column(pa.Float, nullable=True, coerce=True),
    'AMTCUR': Column(pa.String, nullable=True, coerce=True),
    'CUR': Column(pa.String, nullable=True, coerce=True),
    'PAYCUR': Column(pa.String, nullable=True, coerce=True),
    'TMCUR': Column(pa.Float, nullable=True, coerce=True),
    'DPTCOD': Column(pa.Float, nullable=True, coerce=True),
    'DIAMT': Column(pa.Float, nullable=True, coerce=True),
    'IBDAMT': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
