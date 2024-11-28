import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code': Column(pa.String, nullable=True, coerce=True),
    'Insertion Date': Column(pa.String, nullable=True, coerce=True),
    'Cost center code': Column(pa.String, nullable=True, coerce=True),
    'Cost center Name': Column(pa.String, nullable=True, coerce=True),
    'CC Level 1': Column(pa.String, nullable=True, coerce=True),
    'CC Level 2': Column(pa.String, nullable=True, coerce=True),
    'Accounting Date': Column(pa.String, nullable=True, coerce=True),
    'Account No': Column(pa.String, nullable=True, coerce=True),
    'Document no.': Column(pa.Float, nullable=True, coerce=True),
    'Mov. no.': Column(pa.Float, nullable=True, coerce=True),
    'Client Id': Column(pa.Float, nullable=True, coerce=True),
    'Client IATA Code': Column(pa.Float, nullable=True, coerce=True),
    'Amount': Column(pa.Float, nullable=True, coerce=True),
    'Currency': Column(pa.String, nullable=True, coerce=True),
    'Client Name': Column(pa.Float, nullable=True, coerce=True),
    'Type de reporting': Column(pa.String, nullable=True, coerce=True),
    'GL Status': Column(pa.String, nullable=True, coerce=True),
    'Cockpit Code 1': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
