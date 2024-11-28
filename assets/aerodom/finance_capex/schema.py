import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Proyecto': Column(pa.String, nullable=True, coerce=True),
    'Nombre cuenta': Column(pa.String, nullable=True, coerce=True),
    'Cod. Localidad': Column(pa.String, nullable=True, coerce=True),
    'Cod. Area': Column(pa.String, nullable=True, coerce=True),
    'Major categories': Column(pa.String, nullable=True, coerce=True),
    'Categories': Column(pa.String, nullable=True, coerce=True),
    'Sub-categoria': Column(pa.String, nullable=True, coerce=True),
    'Grupo contable proyecto': Column(pa.String, nullable=True, coerce=True),
    'Anual Importe presupuestado': Column(pa.Float, nullable=True, coerce=True),
    'Anual Importe ejecutado': Column(pa.Float, nullable=True, coerce=True),
    'Anual Importe comprometido': Column(pa.Float, nullable=True, coerce=True),
    'Anual importe disponible': Column(pa.Float, nullable=True, coerce=True),
    'Presupuesto 2018-2030': Column(pa.Float, nullable=True, coerce=True),
    'Ejecutado until CY': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
