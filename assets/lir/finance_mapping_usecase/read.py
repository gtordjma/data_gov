import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="Mapping", converters={"Coriport Account - Level 4": str}, engine="openpyxl", nrows=10000)
