import pandas as pd

def read(file):
    return pd.read_excel( file, header=1, converters={"Short Name": str}, engine="openpyxl" , nrows=10000)
