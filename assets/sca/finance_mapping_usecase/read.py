import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="Level 0-1-2-3 + cockpit mapping", converters = {"Level 4 - Local account code": str}, engine="openpyxl", nrows=10000)
