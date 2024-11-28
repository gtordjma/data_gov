import pandas as pd

def read(file):
    return pd.read_csv( file, sep=";", encoding="latin-1" , skiprows=2, converters={"N° compte": str, "Section": str}, nrows=10000)
