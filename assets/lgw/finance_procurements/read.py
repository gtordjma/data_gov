import pandas as pd

def read(file):
    return pd.read_csv(file, nrows=10000)
