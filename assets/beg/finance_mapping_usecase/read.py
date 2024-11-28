import pandas as pd

def read(file):
    return pd.read_excel(file, sheet_name="MAPPING SDH", engine="openpyxl", nrows=10000)
