import pandas as pd

def read(file):
    return pd.read_csv(file, sep=";", converters = { "Account no.": str, "Document no.": str, "Mov. no.": str, "Cockpit Code 1": str, "Cost center code": str, }, nrows=10000)
