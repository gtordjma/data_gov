import pandas as pd

def read(file):
    return pd.read_excel(file, converters = { "Codigo Cli/For" : str, "Código da conta": str, "Código do centro": str, "Nro Origem" : str, "Filial": float, }, engine="openpyxl", nrows=10000)
