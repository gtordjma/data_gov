import pandas as pd

def read(file):
    return pd.read_excel(file, converters={"Customer code": str}, engine="openpyxl", nrows=10000)
