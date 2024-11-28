import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Sociedad': Column(pa.String, nullable=True, coerce=True),
    'Cuenta': Column(pa.Float, nullable=True, coerce=True),
    'Sociedad GL asociada': Column(pa.Float, nullable=True, coerce=True),
    'Nº documento': Column(pa.Float, nullable=True, coerce=True),
    'Clase de documento': Column(pa.String, nullable=True, coerce=True),
    'Fe.contabilización': Column(pa.DateTime, nullable=True, coerce=True),
    'Clave contabiliz.': Column(pa.Float, nullable=True, coerce=True),
    'Centro de coste': Column(pa.String, nullable=True, coerce=True),
    'Elemento PEP': Column(pa.String, nullable=True, coerce=True),
    'Importe en moneda local': Column(pa.Float, nullable=True, coerce=True),
    'Moneda local': Column(pa.String, nullable=True, coerce=True),
    'Indicador impuestos': Column(pa.String, nullable=True, coerce=True),
    'Doc.compensación': Column(pa.Float, nullable=True, coerce=True),
    'Centro de beneficio': Column(pa.String, nullable=True, coerce=True),
    'Segmento': Column(pa.String, nullable=True, coerce=True),
    'Asignación': Column(pa.String, nullable=True, coerce=True),
    'Texto': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
