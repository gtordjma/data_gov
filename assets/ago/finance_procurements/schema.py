import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Dossier': Column(pa.Float, nullable=True, coerce=True),
    'Date situation': Column(pa.String, nullable=True, coerce=True),
    'Echeancier': Column(pa.String, nullable=True, coerce=True),
    'Section': Column(pa.Float, nullable=True, coerce=True),
    'Libelle section': Column(pa.String, nullable=True, coerce=True),
    'Analyse': Column(pa.String, nullable=True, coerce=True),
    'Tiers': Column(pa.Float, nullable=True, coerce=True),
    'Libelle tiers': Column(pa.String, nullable=True, coerce=True),
    'Piece comptable': Column(pa.String, nullable=True, coerce=True),
    'Date comptable': Column(pa.String, nullable=True, coerce=True),
    'JA': Column(pa.Float, nullable=True, coerce=True),
    'Libelle piece': Column(pa.String, nullable=True, coerce=True),
    'Reference piece': Column(pa.String, nullable=True, coerce=True),
    'Date echeance': Column(pa.String, nullable=True, coerce=True),
    '+ 90 jours': Column(pa.String, nullable=True, coerce=True),
    '61-90 jours': Column(pa.String, nullable=True, coerce=True),
    '31-60 jours': Column(pa.String, nullable=True, coerce=True),
    '- 30 jours': Column(pa.String, nullable=True, coerce=True),
    'Non Echues': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
