import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Code Site': Column(pa.String, nullable=True, coerce=True),
    'Code Version': Column(pa.String, nullable=True, coerce=True),
    'Mois': Column(pa.String, nullable=True, coerce=True),
    'Année': Column(pa.Float, nullable=True, coerce=True),
    'Code Organigramme': Column(pa.String, nullable=True, coerce=True),
    'Code Rubrique': Column(pa.String, nullable=True, coerce=True),
    'Code P/R': Column(pa.String, nullable=True, coerce=True),
    'Code Analytique': Column(pa.Float, nullable=True, coerce=True),
    'Code Effectif': Column(pa.String, nullable=True, coerce=True),
    'Code Investissement': Column(pa.Float, nullable=True, coerce=True),
    'Code Mesure': Column(pa.String, nullable=True, coerce=True),
    'Code Site Destinataires': Column(pa.Float, nullable=True, coerce=True),
    'Code Destinataires': Column(pa.Float, nullable=True, coerce=True),
    'Capacité': Column(pa.String, nullable=True, coerce=True),
    'Charge': Column(pa.String, nullable=True, coerce=True),
    'Montant': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
