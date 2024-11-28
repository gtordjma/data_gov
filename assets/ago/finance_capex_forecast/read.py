import pandas as pd

def read(file):
    return pd.read_csv(file, sep=";", encoding="latin-1", converters={"Mois": str}, nrows=10000)
