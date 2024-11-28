import pandas as pd

def read(file):
    return pd.read_excel( file, skiprows=1, converters={"Projeto": str}, engine="openpyxl" , nrows=10000)
