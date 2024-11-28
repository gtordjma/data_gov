import pandas as pd

def read(file):
    return pd.read_excel(file, skiprows=18, engine="openpyxl", nrows=10000)
