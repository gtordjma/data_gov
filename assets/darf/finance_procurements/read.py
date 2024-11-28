import pandas as pd

def read(file):
    return pd.read_csv(file, sep=";", converters =  { "Code Tiers": str, "N° échéance (H technique)": str, "N°  échéance (technique)": str, "Compte Comptable": str, }, nrows=10000)
