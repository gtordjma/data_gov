import pandas as pd

def read(file):
    return pd.read_csv(file, sep=",", converters = {"site": str, "compte_ana": str, "num_piece": str, "axe_orga": str}, encoding="utf-16", nrows=10000)
