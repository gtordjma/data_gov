import pandas as pd

def read(file):
    return pd.read_csv(file, sep=",", converters = {"code_tiers": str, "num_echeance": str, "compte_comptable": str}, encoding="utf-16", nrows=10000)
