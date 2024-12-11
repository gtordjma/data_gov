import pandera as pa
from pandera import Column, DataFrameSchema, Index

schema = DataFrameSchema(
    columns={
        'CODE_ANALYTIQUE': Column(pa.Int, nullable=False, coerce=True),
        'LIBELLE_DU_CODE_ANALYTIQUE': Column(pa.String, nullable=False, coerce=True),
        'Code Section/Projets': Column(pa.String, nullable=True, coerce=True),
        'Code Analytique et Section': Column(pa.String, nullable=True, coerce=True),
        'Code Projet': Column(pa.String, nullable=True, coerce=True),
    },
    index=Index(pa.Int, nullable=False, coerce=True),
    strict=True,
    coerce=True,
)