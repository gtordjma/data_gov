import pandas as pd

def read(file):
    return pd.read_excel( file, engine="openpyxl", header=0, converters={"ACCTID": str} , nrows=10000)
