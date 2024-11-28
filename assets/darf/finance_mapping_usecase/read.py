import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="Mapping", converters = { "Local account number": str, "Hierarchy Level 0": str, "Hierarchy Level 1": str, "Hierarchy Level 2": str, }, engine="openpyxl" , nrows=10000)
