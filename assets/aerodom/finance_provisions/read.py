import pandas as pd

def read(file):
    return pd.read_excel( file, engine="openpyxl", sheet_name="Clients provisions", header=1, skiprows=1, nrows=10000)
