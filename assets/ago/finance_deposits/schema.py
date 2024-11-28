import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'nb_client': Column(pa.Float, nullable=True, coerce=True),
    'client_name': Column(pa.String, nullable=True, coerce=True),
    'guarante_type': Column(pa.String, nullable=True, coerce=True),
    'guarante_montant_nte': Column(pa.String, nullable=True, coerce=True),
    'guarante_montant_snr': Column(pa.Float, nullable=True, coerce=True),
    'depot_guarante_nte': Column(pa.String, nullable=True, coerce=True),
    'depot_guarante_snr': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
