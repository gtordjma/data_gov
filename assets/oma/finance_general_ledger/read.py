import pandas as pd

def read(file):
    return pd.read_excel(file, converters={"Sociedad": str}, engine="openpyxl", nrows=10000)
