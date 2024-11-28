import pandas as pd

def read(file):
    return pd.read_csv( file, sep=",", converters={ "Customer Account - Key": str, "Charge local ID ": str, "GL Account no.": str, }, encoding="latin-1", nrows=10000)
