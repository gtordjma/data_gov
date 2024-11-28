import pandas as pd

def read(file):
    return pd.read_excel(file, skiprows=5, header=None, engine="openpyxl", nrows=10000)
