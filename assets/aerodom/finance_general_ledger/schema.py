import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Fecha registro': Column(pa.DateTime, nullable=True, coerce=True),
    'Tipo contrapartida': Column(pa.String, nullable=True, coerce=True),
    'Tipo documento': Column(pa.String, nullable=True, coerce=True),
    'Nº documento': Column(pa.String, nullable=True, coerce=True),
    'Nº documento externo': Column(pa.String, nullable=True, coerce=True),
    'Nº cuenta': Column(pa.Float, nullable=True, coerce=True),
    'Nombre': Column(pa.String, nullable=True, coerce=True),
    'Nombre Cuenta': Column(pa.String, nullable=True, coerce=True),
    'Cta. contrapartida': Column(pa.String, nullable=True, coerce=True),
    'Descripción': Column(pa.String, nullable=True, coerce=True),
    'Code Localidad': Column(pa.String, nullable=True, coerce=True),
    'Code Area': Column(pa.String, nullable=True, coerce=True),
    'Importe': Column(pa.Float, nullable=True, coerce=True),
    'Importe divisa-adicional': Column(pa.Float, nullable=True, coerce=True),
    'Nº proyecto': Column(pa.String, nullable=True, coerce=True),
    'Nº mov.': Column(pa.Float, nullable=True, coerce=True),
    'Seguimiento tesoreria': Column(pa.String, nullable=True, coerce=True),
    'Id. usuario': Column(pa.String, nullable=True, coerce=True),
    'A/F Nº mov.': Column(pa.Float, nullable=True, coerce=True),
    'A/F Tipo mov.': Column(pa.String, nullable=True, coerce=True),
    'Asiento automático': Column(pa.Bool, nullable=True, coerce=True),
    'Asiento post-cierre': Column(pa.Float, nullable=True, coerce=True),
    'Cantidad': Column(pa.Float, nullable=True, coerce=True),
    'Cód. auditoría': Column(pa.String, nullable=True, coerce=True),
    'Cód. origen': Column(pa.String, nullable=True, coerce=True),
    'Cód. origen2': Column(pa.String, nullable=True, coerce=True),
    'Cód. procedencia mov.': Column(pa.String, nullable=True, coerce=True),
    'IATA Code': Column(pa.String, nullable=True, coerce=True),
    'Código socio IC': Column(pa.Float, nullable=True, coerce=True),
    'Corporativo 1': Column(pa.String, nullable=True, coerce=True),
    'Corporativo 2': Column(pa.String, nullable=True, coerce=True),
    'Debe div.-adic.': Column(pa.Float, nullable=True, coerce=True),
    'Grupo contable negocio': Column(pa.String, nullable=True, coerce=True),
    'Grupo contable producto': Column(pa.String, nullable=True, coerce=True),
    'Haber div.-adic.': Column(pa.Float, nullable=True, coerce=True),
    'Importe debe': Column(pa.Float, nullable=True, coerce=True),
    'Importe haber': Column(pa.Float, nullable=True, coerce=True),
    'Importe IVA': Column(pa.Float, nullable=True, coerce=True),
    'Nº de cuenta antiguo': Column(pa.Float, nullable=True, coerce=True),
    'Nº efecto': Column(pa.Float, nullable=True, coerce=True),
    'Nº movimiento revertido': Column(pa.Float, nullable=True, coerce=True),
    'No. Comprobante Fiscal': Column(pa.String, nullable=True, coerce=True),
    'Revertido': Column(pa.Bool, nullable=True, coerce=True),
    'Revertido por el movimiento nº': Column(pa.Float, nullable=True, coerce=True),
    'Tipo IVA': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
