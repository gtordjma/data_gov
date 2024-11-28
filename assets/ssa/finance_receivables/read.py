import pandas as pd

def read(file):
    return pd.read_excel(file, converters = { "NossoNumero": str, "CardCode": str, "ValorDoBoleto": float, "SituacaoCR": str, }, engine="openpyxl", nrows=10000)
