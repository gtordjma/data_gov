import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="SDH - Clients guarantees", engine="openpyxl" , nrows=10000)
