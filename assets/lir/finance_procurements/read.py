import pandas as pd

def read(file):
    return pd.read_excel(file, header=20, engine="openpyxl", nrows=10000)
