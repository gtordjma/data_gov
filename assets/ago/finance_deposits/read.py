import pandas as pd

def read(file):
    return pd.read_csv( file, sep=";", encoding="latin-1", skiprows=1, header=0, names=[ "nb_client", "client_name", "guarante_type", "guarante_montant_nte", "guarante_montant_snr", "depot_guarante_nte", "depot_guarante_snr", ], nrows=10000)
