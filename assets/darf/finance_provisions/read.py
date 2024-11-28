import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="Clients provisions", converters = {"Accounting Client code": str}, engine="openpyxl", nrows=10000)
