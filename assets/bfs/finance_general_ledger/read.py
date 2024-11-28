import pandas as pd

def read(file):
    return pd.read_csv( file, sep=",", quotechar='"', encoding="latin-1", converters={"CostCentre": str, "MainAccount": str}, nrows=10000)
