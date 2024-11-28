import pandas as pd

def read(file):
    return pd.read_csv(file, sep="\t", nrows=10000)
