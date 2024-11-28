import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Nombre 1': Column(pa.String, nullable=True, coerce=True),
    'Cuenta': Column(pa.Float, nullable=True, coerce=True),
    'Referencia': Column(pa.String, nullable=True, coerce=True),
    'Fecha de documento': Column(pa.DateTime, nullable=True, coerce=True),
    'Vencimiento neto': Column(pa.DateTime, nullable=True, coerce=True),
    'Importe en moneda local': Column(pa.Float, nullable=True, coerce=True),
    'ML': Column(pa.String, nullable=True, coerce=True),
    'Doc.compensación': Column(pa.Float, nullable=True, coerce=True),
    'Texto': Column(pa.String, nullable=True, coerce=True),
    'Asignación': Column(pa.String, nullable=True, coerce=True),
    'Clase de documento': Column(pa.String, nullable=True, coerce=True),
    'Cuenta de mayor': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
