import pandas as pd

def read(file):
    return pd.read_csv( file, sep="\t", skiprows=1, header=0, names=[ "year", "version", "airportIATACode", "A", "B", "C", "D", "E", "F", "G", "month", "type", "amount", ], nrows=10000)
