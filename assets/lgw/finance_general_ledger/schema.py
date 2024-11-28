import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'Airport Code,Insertion Date,Cost center code,Cost center Name,CC Level 1,CC Level 2,Accounting Date,Account no.,Document no.,Mov. no.,Client Id,Client IATA Code,Amount,Currency,Client Name,Type de reporting,GL Status,Cockpit Code 1': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
