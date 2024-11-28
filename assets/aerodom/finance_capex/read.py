import pandas as pd

def read(file):
    return pd.read_excel(file, header=3, engine="openpyxl", nrows=10000)
