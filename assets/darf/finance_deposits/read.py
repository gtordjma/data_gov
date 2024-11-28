import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="Clients deposits", converters = {"Accounting Client code": str}, engine="openpyxl", nrows=10000)
