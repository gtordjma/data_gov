import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'PAYEUR': Column(pa.String, nullable=True, coerce=True),
    'INTITULE': Column(pa.String, nullable=True, coerce=True),
    'PIECE': Column(pa.String, nullable=True, coerce=True),
    'DATE': Column(pa.String, nullable=True, coerce=True),
    'JA': Column(pa.String, nullable=True, coerce=True),
    'LIBELLE': Column(pa.String, nullable=True, coerce=True),
    'DATECH': Column(pa.String, nullable=True, coerce=True),
    'MR': Column(pa.Float, nullable=True, coerce=True),
    'CT': Column(pa.Float, nullable=True, coerce=True),
    'PAIEMENT': Column(pa.Float, nullable=True, coerce=True),
    'FACT ECH': Column(pa.String, nullable=True, coerce=True),
    'FACT NON ECH': Column(pa.String, nullable=True, coerce=True),
    'LETTRE': Column(pa.String, nullable=True, coerce=True),
    'CREDIT': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
