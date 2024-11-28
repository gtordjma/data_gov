import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Sociedad': Column(pa.String, nullable=True, coerce=True),
    'Fe.contabilización': Column(pa.DateTime, nullable=True, coerce=True),
    'Cuenta de mayor': Column(pa.Float, nullable=True, coerce=True),
    'Centro de coste': Column(pa.String, nullable=True, coerce=True),
    'Importe': Column(pa.Float, nullable=True, coerce=True),
    'Moneda': Column(pa.String, nullable=True, coerce=True),
    'Importe ML': Column(pa.Float, nullable=True, coerce=True),
    'Moneda local': Column(pa.String, nullable=True, coerce=True),
    'Tipo de cambio': Column(pa.Float, nullable=True, coerce=True),
    'Clave contabiliz.': Column(pa.Float, nullable=True, coerce=True),
    'Indicador Debe/Haber': Column(pa.String, nullable=True, coerce=True),
    'Ejercicio': Column(pa.Float, nullable=True, coerce=True),
    'Posición': Column(pa.Float, nullable=True, coerce=True),
    'Nº documento': Column(pa.Float, nullable=True, coerce=True),
    'Clase de documento': Column(pa.String, nullable=True, coerce=True),
    'ClientIATACode': Column(pa.Float, nullable=True, coerce=True),
    'Cliente': Column(pa.String, nullable=True, coerce=True),
    'Nombre de Deudor': Column(pa.String, nullable=True, coerce=True),
    'Acreedor': Column(pa.Float, nullable=True, coerce=True),
    'Nombre de Acreedor': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
