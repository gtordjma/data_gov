import pandas as pd

def read(file):
    return pd.read_excel( file, skiprows=10, usecols=list(range(1, 60)), engine="openpyxl", nrows=10000)
