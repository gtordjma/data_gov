import pandas as pd

def read(file):
    return pd.read_csv( file, delimiter="\t", names=[ "year", "Version", "unamed1", "activity code", "unamed2", "f", "g", "h", "i", "reporting", "month", "account code", "amountValue", ], skiprows=1, converters = {"account code": str, "activity code": str}, nrows=10000)
