import pandas as pd

def read(file):
    return pd.read_csv( file, delimiter="\t", names=[ "FY", "SCEN.", "ORGA", "ACTIVITY", "Projet", "Supplier", "BU", "Type", "View", "Reporting", "accountingDate", "accountId", "mesure", ], skiprows=1, nrows=10000)
