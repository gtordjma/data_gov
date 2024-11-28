import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="Clients Guarantees", header=6, converters={"Client code": float}, engine="openpyxl", nrows=10000)
