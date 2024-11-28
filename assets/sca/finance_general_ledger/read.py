import pandas as pd

def read(file):
    return pd.read_excel( file, converters={"Account Number": str, "Debits": float, "Credits": float}, engine="openpyxl", nrows=10000)
