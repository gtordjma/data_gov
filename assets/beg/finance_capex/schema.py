import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Unnamed: 0': Column(pa.Float, nullable=True, coerce=True),
    'CAPEX Cumulative Figures
(K EUR)': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 2': Column(pa.String, nullable=True, coerce=True),
    'TOTAL CAPEX': Column(pa.Float, nullable=True, coerce=True),
    'Works - EPC incl price adjsutment': Column(pa.Float, nullable=True, coerce=True),
    'Works & Equip. - Non EPC': Column(pa.Float, nullable=True, coerce=True),
    'Op. & Maint. CAPEX': Column(pa.Float, nullable=True, coerce=True),
    'HMR Infrastructure': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
