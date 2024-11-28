import pandas as pd

def read(file):
    return pd.read_csv(file, encoding="latin1", sep=";", nrows=10000)
