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
    'Enero': Column(pa.Float, nullable=True, coerce=True),
    'Febrero': Column(pa.Float, nullable=True, coerce=True),
    'Marzo': Column(pa.Float, nullable=True, coerce=True),
    'Abril': Column(pa.Float, nullable=True, coerce=True),
    'Mayo': Column(pa.Float, nullable=True, coerce=True),
    'Junio': Column(pa.Float, nullable=True, coerce=True),
    'Julio': Column(pa.Float, nullable=True, coerce=True),
    'Agosto': Column(pa.Float, nullable=True, coerce=True),
    'Septiembre': Column(pa.Float, nullable=True, coerce=True),
    'Octubre': Column(pa.Float, nullable=True, coerce=True),
    'Noviembre': Column(pa.Float, nullable=True, coerce=True),
    'Diciembre': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
