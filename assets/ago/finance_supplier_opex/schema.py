import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'CPTGEN': Column(pa.String, nullable=True, coerce=True),
    'NOM': Column(pa.String, nullable=True, coerce=True),
    'DATE': Column(pa.String, nullable=True, coerce=True),
    'JA': Column(pa.String, nullable=True, coerce=True),
    'PIECE': Column(pa.String, nullable=True, coerce=True),
    'LIBELLE': Column(pa.String, nullable=True, coerce=True),
    'MANDAT': Column(pa.Float, nullable=True, coerce=True),
    'RT': Column(pa.String, nullable=True, coerce=True),
    'DEBIT': Column(pa.String, nullable=True, coerce=True),
    'LT': Column(pa.String, nullable=True, coerce=True),
    'CREDIT': Column(pa.String, nullable=True, coerce=True),
    'SC': Column(pa.Float, nullable=True, coerce=True),
    'TPIECE': Column(pa.String, nullable=True, coerce=True),
    'QUANTITE': Column(pa.String, nullable=True, coerce=True),
    'MONNAIE': Column(pa.String, nullable=True, coerce=True),
    'STAT1': Column(pa.String, nullable=True, coerce=True),
    'STAT2': Column(pa.String, nullable=True, coerce=True),
    'STAT3': Column(pa.String, nullable=True, coerce=True),
    'STAT4': Column(pa.String, nullable=True, coerce=True),
    'STAT5': Column(pa.String, nullable=True, coerce=True),
    'MARCHE': Column(pa.Float, nullable=True, coerce=True),
    'DATE DEBUT CUT OFF': Column(pa.String, nullable=True, coerce=True),
    'DATE FIN CUT OFF': Column(pa.String, nullable=True, coerce=True),
    'NUM ENGAGEMENT': Column(pa.Float, nullable=True, coerce=True),
    'STATUT ENGAGEMENT': Column(pa.Float, nullable=True, coerce=True),
    'DATE ENGAGEMENT': Column(pa.Float, nullable=True, coerce=True),
    'COMPTE AXE 0': Column(pa.String, nullable=True, coerce=True),
    'MONTANT AXE 0': Column(pa.String, nullable=True, coerce=True),
    'QUANTITE AXE 0': Column(pa.String, nullable=True, coerce=True),
    'DOSSIER': Column(pa.Float, nullable=True, coerce=True),
    'OPERATEUR': Column(pa.String, nullable=True, coerce=True),
    'DATE DE SAISIE': Column(pa.String, nullable=True, coerce=True),
    'DATE DE COMPTABILISATION': Column(pa.String, nullable=True, coerce=True),
    'DATE LETTRAGE': Column(pa.String, nullable=True, coerce=True),
    'Unnamed: 34': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)