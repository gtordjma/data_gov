import pandas as pd

def read(file):
    return pd.read_excel( file, engine="openpyxl", header=0, converters={ "ACSEGVAL02": str, "ACCOUNTEXSEG": str, "ENTRYNBR": str, "BATCHNO": str, "POSTINGSEQ": str, }, nrows=10000)
