import pandas as pd

def read(file):
    return pd.read_excel(file, engine="openpyxl", skiprows=8, nrows=10000)
