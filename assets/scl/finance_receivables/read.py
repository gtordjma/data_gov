import pandas as pd

def read(file):
    return pd.read_excel( file, header=0, converters={"Cuenta": float}, engine="openpyxl" , nrows=10000)
