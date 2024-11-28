import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Project Manager': Column(pa.String, nullable=True, coerce=True),
    'Geographical area': Column(pa.String, nullable=True, coerce=True),
    'Project ID': Column(pa.Float, nullable=True, coerce=True),
    'Project Name': Column(pa.String, nullable=True, coerce=True),
    'Project Typology': Column(pa.String, nullable=True, coerce=True),
    'Project Category_1': Column(pa.String, nullable=True, coerce=True),
    'Project Category_2': Column(pa.String, nullable=True, coerce=True),
    'Project Category_3': Column(pa.String, nullable=True, coerce=True),
    'Green Capex': Column(pa.String, nullable=True, coerce=True),
    'Perfil 
Investimento': Column(pa.String, nullable=True, coerce=True),
    'Extraction Date': Column(pa.Float, nullable=True, coerce=True),
    'Version': Column(pa.String, nullable=True, coerce=True),
    'Version_Year': Column(pa.Float, nullable=True, coerce=True),
    'Version2': Column(pa.String, nullable=True, coerce=True),
    'MES': Column(pa.String, nullable=True, coerce=True),
    'ANO': Column(pa.String, nullable=True, coerce=True),
    'Value': Column(pa.Float, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
