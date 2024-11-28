import pandas as pd

def read(file):
    return pd.read_excel( file, engine="openpyxl", sheet_name="Clients deposits", header=1, skiprows=0 , nrows=10000)
