import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Centro de coste': Column(pa.String, nullable=False, coerce=True),
    'Sociedad': Column(pa.String, nullable=False, coerce=True),
    'Centro de beneficio': Column(pa.String, nullable=False, coerce=True),
    'Denominación': Column(pa.String, nullable=False, coerce=True),
    'Descripción': Column(pa.String, nullable=False, coerce=True),
    'Texto breve CeCo': Column(pa.String, nullable=False, coerce=True),
},
    strict=True,
    coerce=True,
)