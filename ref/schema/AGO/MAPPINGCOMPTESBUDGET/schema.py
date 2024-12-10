import pandera as pa
from pandera import Column, DataFrameSchema,Index

schema = DataFrameSchema(
    columns={
        'Code rubrique : Opteva (Fichier d\'import)': Column(pa.String, nullable=False, coerce=True),
        'Compte Comptable': Column(pa.Int, nullable=False, coerce=True),
        'Libellé Compte Comptable': Column(pa.String, nullable=False, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)

