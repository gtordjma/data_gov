import pandera as pa
from pandera import Column, DataFrameSchema

schema = DataFrameSchema({
    'textbox13': Column(pa.String, nullable=True, coerce=True),
    'Textbox931': Column(pa.String, nullable=True, coerce=True),
    'Textbox3': Column(pa.String, nullable=True, coerce=True),
    'textbox143': Column(pa.Float, nullable=True, coerce=True),
    'textbox134': Column(pa.String, nullable=True, coerce=True),
    'CustGroup': Column(pa.String, nullable=True, coerce=True),
    'Textbox66': Column(pa.Float, nullable=True, coerce=True),
    'Textbox68': Column(pa.Float, nullable=True, coerce=True),
    'Textbox70': Column(pa.Float, nullable=True, coerce=True),
    'HeadingAgingBucketDescription05': Column(pa.Float, nullable=True, coerce=True),
    'HeadingAgingBucketDescription06': Column(pa.Float, nullable=True, coerce=True),
    'HeadingAgingBucketDescription07': Column(pa.Float, nullable=True, coerce=True),
    'Textbox108': Column(pa.String, nullable=True, coerce=True),
    'textbox224': Column(pa.String, nullable=True, coerce=True),
    'textbox225': Column(pa.String, nullable=True, coerce=True),
    'textbox226': Column(pa.String, nullable=True, coerce=True),
    'textbox227': Column(pa.String, nullable=True, coerce=True),
    'textbox228': Column(pa.String, nullable=True, coerce=True),
    'textbox182': Column(pa.Float, nullable=True, coerce=True),
    'Textbox1564': Column(pa.String, nullable=True, coerce=True),
    'textbox229': Column(pa.String, nullable=True, coerce=True),
    'textbox267': Column(pa.String, nullable=True, coerce=True),
    'textbox268': Column(pa.String, nullable=True, coerce=True),
    'textbox269': Column(pa.String, nullable=True, coerce=True),
    'textbox270': Column(pa.String, nullable=True, coerce=True),
    'textbox271': Column(pa.String, nullable=True, coerce=True),
    'textbox272': Column(pa.String, nullable=True, coerce=True),
    'textbox273': Column(pa.String, nullable=True, coerce=True),
    'TransDate2': Column(pa.String, nullable=True, coerce=True),
    'Voucher2': Column(pa.String, nullable=True, coerce=True),
    'Balance2': Column(pa.Float, nullable=True, coerce=True),
    'vlookup due date': Column(pa.String, nullable=True, coerce=True),
    'Balance23': Column(pa.Float, nullable=True, coerce=True),
    'Balance32': Column(pa.Float, nullable=True, coerce=True),
    'Balance42': Column(pa.Float, nullable=True, coerce=True),
    'Balance52': Column(pa.Float, nullable=True, coerce=True),
    'Balance62': Column(pa.Float, nullable=True, coerce=True),
    'Balance72': Column(pa.Float, nullable=True, coerce=True),
    'textbox125': Column(pa.String, nullable=True, coerce=True),
    'textbox281': Column(pa.Float, nullable=True, coerce=True),
    'textbox282': Column(pa.Float, nullable=True, coerce=True),
    'textbox283': Column(pa.Float, nullable=True, coerce=True),
    'textbox284': Column(pa.Float, nullable=True, coerce=True),
    'textbox285': Column(pa.Float, nullable=True, coerce=True),
    'textbox286': Column(pa.Float, nullable=True, coerce=True),
    'textbox287': Column(pa.Float, nullable=True, coerce=True),
    'textbox288': Column(pa.String, nullable=True, coerce=True),
    'textbox289': Column(pa.String, nullable=True, coerce=True),
    'textbox290': Column(pa.String, nullable=True, coerce=True),
    'textbox291': Column(pa.String, nullable=True, coerce=True),
    'textbox292': Column(pa.String, nullable=True, coerce=True),
    'textbox293': Column(pa.String, nullable=True, coerce=True),
    'textbox294': Column(pa.String, nullable=True, coerce=True),
    'textbox295': Column(pa.String, nullable=True, coerce=True),
    'textbox296': Column(pa.Float, nullable=True, coerce=True),
    'textbox297': Column(pa.Float, nullable=True, coerce=True),
    'textbox298': Column(pa.Float, nullable=True, coerce=True),
    'textbox299': Column(pa.Float, nullable=True, coerce=True),
    'textbox300': Column(pa.Float, nullable=True, coerce=True),
    'textbox301': Column(pa.Float, nullable=True, coerce=True),
    'textbox302': Column(pa.Float, nullable=True, coerce=True),
    'textbox118': Column(pa.String, nullable=True, coerce=True),
    'textbox303': Column(pa.String, nullable=True, coerce=True),
    'textbox304': Column(pa.String, nullable=True, coerce=True),
    'textbox305': Column(pa.String, nullable=True, coerce=True),
    'textbox306': Column(pa.String, nullable=True, coerce=True),
    'textbox307': Column(pa.String, nullable=True, coerce=True),
    'textbox308': Column(pa.String, nullable=True, coerce=True),
},
    strict=True,
    coerce=True,
)
