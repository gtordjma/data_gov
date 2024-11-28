import pandas as pd

def read(file):
    return pd.read_excel(file, engine="openpyxl", nrows=10000)
