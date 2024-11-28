import pandas as pd

def read(file):
    return pd.read_csv(file, sep=",", converters={"Account No": str}, nrows=10000)
