import pandas as pd

def read(file):
    return pd.read_csv( file, sep=";", encoding="latin-1", converters={"PIECE": str, "CPTGEN": str} , nrows=10000)
