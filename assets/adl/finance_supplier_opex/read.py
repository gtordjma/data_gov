import pandas as pd

def read(file):
    return pd.read_csv(file, sep=";", encoding="ISO-8859-1", nrows=10000)
