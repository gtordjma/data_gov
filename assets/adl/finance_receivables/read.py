import pandas as pd

def read(file):
    return pd.read_csv(file, sep=";", encoding="latin-1", nrows=10000)
