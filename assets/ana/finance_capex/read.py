import pandas as pd

def read(file):
    return pd.read_excel(file, converters={"MES": str, "ANO": str}, engine="openpyxl", nrows=10000)
