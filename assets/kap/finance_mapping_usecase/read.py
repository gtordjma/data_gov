import pandas as pd

def read(file):
    return pd.read_excel( file, sheet_name="Level 0-1-2-3 + cockpit map_KAP", engine="openpyxl" , nrows=10000)
