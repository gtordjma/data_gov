import pandas as pd

def read(file):
    return pd.read_csv(file, sep=",", thousands=",", nrows=10000)
