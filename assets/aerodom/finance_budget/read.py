import pandas as pd

def read(file):
    return pd.read_excel(file, engine="openpyxl", header=0, skiprows=4, nrows=10000)
