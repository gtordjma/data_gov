import os
from typing import Callable, Dict

import numpy as np
import pandas_gbq

from data_gov.use_cases.finance.FinanceFileTypes import FinanceFileTypes

GCP_PROJECT = os.getenv('GCP_PROJECT')


def df_to_array(df):
    # Convert column names and all data to string format and build the result
    result = [df.columns.tolist()] + df.astype(str).values.tolist()
    return result


def finance_deposits_kpis(file):
    kpis = {}
    df = pd.read_parquet(file)
    kpis["deposits_kpi"] = [["amountValue"], [f"{df['amountValue'].sum():,.0f}".replace(",", " ")]]
    tab = (df.groupby('customerName', as_index=False)
           .agg(amountSum=('amountValue', lambda x: round(x.sum(), 2)))
           .assign(amountSum=lambda df: df['amountSum'].abs())
           .sort_values(by='amountSum', ascending=False)
           .head(5))[['customerName', 'amountSum']]
    tab['amountSum'] = tab['amountSum'].apply(lambda x: f"{x:,.0f}".replace(",", " "))
    kpis["deposits_top_five"] = df_to_array(tab)
    return kpis


def finance_guarantees_kpis(file):
    kpis = {}
    df = pd.read_parquet(file)
    kpis["guarantees_kpi"] = [["amountValue"], [f"{df['amountValue'].sum():,.0f}".replace(",", " ")]]
    tab = (df.groupby('customerName', as_index=False)
           .agg(amountSum=('amountValue', lambda x: round(x.sum(), 2)))
           .assign(amountSum=lambda df: df['amountSum'].abs())
           .sort_values(by='amountSum', ascending=False)
           .head(5))[['customerName', 'amountSum']]
    tab['amountSum'] = tab['amountSum'].apply(lambda x: f"{x:,.0f}".replace(",", " "))
    kpis["guarantees_top_five"] = df_to_array(tab)
    return kpis


def finance_capex_forecast_kpis(file):
    kpis = {}
    df = pd.read_parquet(file)
    kpis["cpxforecast_kpi"] = [["amountPlannedMonth"], [f"{df['amountPlannedMonth'].sum():,.0f}".replace(",", " ")]]
    tab = (df.groupby('version', as_index=False)
           .agg(amountSum=('amountPlannedMonth', lambda x: round(x.sum(), 2)))
           .assign(amountSum=lambda df: df['amountSum'].abs())
           .sort_values(by='amountSum', ascending=False)
           .head(5))[['version', 'amountSum']]
    tab['amountSum'] = tab['amountSum'].apply(lambda x: f"{x:,.0f}".replace(",", " "))
    kpis["cpxforecast_top_five"] = df_to_array(tab)
    return kpis


def ar(df):
    df['dueDate'] = pd.to_datetime(df['dueDate'], errors='coerce')
    df['extractDate'] = pd.to_datetime(df['extractDate'], errors='coerce')

    # Création de la colonne `statusDept`
    df['statusDept'] = np.where(df['dueDate'] <= df['extractDate'], 'Not Expired', 'Expired')
    df['amountValue'] = df['amountValue'].fillna(0)
    # Agrégation et transformation avec ingestionId et etl_ds
    grouped_df = (
        df
        .groupby(['folderId', 'ingestionId', 'statusDept', 'etl_ds'], as_index=False)
        .agg(total=('amountValue', lambda x: round(x.sum(), 2)))
        .sort_values(by='etl_ds', ascending=False)
    )
    grouped_df['total'] = grouped_df['total'].apply(lambda x: f"{x:,.0f}".replace(",", " "))

    return grouped_df[['statusDept', 'total']]


def finance_receivables_kpis(file):
    kpis = {}
    df = pd.read_parquet(file)
    # Extraire les informations de partition
    etl_ds = file.split("etl_ds=")[1].split("/")[0]
    ingestion_id = file.split("ingestionId=")[1].split("/")[0]

    # Ajouter les colonnes
    df['etl_ds'] = etl_ds
    df['ingestionId'] = ingestion_id

    kpis["receivables_kpi"] = df_to_array(ar(df))
    tab = (df.groupby('customerName', as_index=False)
           .agg(amountSum=('amountValue', lambda x: round(x.sum(), 2)))
           .assign(amountSum=lambda df: df['amountSum'].abs())
           .sort_values(by='amountSum', ascending=False)
           .head(5))[['customerName', 'amountSum']]
    tab['amountSum'] = tab['amountSum'].apply(lambda x: f"{x:,.0f}".replace(",", " "))
    kpis["receivables_top_five"] = df_to_array(tab)
    return kpis


# 'level0', 'appSheetId','runId', 'userEmail',

def gl(df):
    df['year'] = pd.to_datetime(df['accountingDate']).dt.year
    max_date = pd.to_datetime(df['accountingDate']).max()
    df['month'] = max_date.month
    print(df[['month', 'level0', 'accountCostCenterCode', 'amountValue']].head())

    df_grouped = df.groupby(['month', 'year', 'level0'], as_index=False)
    final = df_grouped.agg(sum_by_level_0=('amountValue', lambda x: round(x.sum(), 2)))

    result_df = final[['year', 'month', 'level0', 'sum_by_level_0']]
    result_df['sum_by_level_0'] = result_df['sum_by_level_0'].apply(format_amount)

    return result_df


def finance_general_ledger_kpis(file):
    kpis = {}
    df = pd.read_parquet(file)

    etl_ds = file.split("etl_ds=")[1].split("/")[0]
    ingestion_id = file.split("ingestionId=")[1].split("/")[0]
    df['etl_ds'] = etl_ds
    df['ingestionId'] = ingestion_id

    query = f"""SELECT *  from `finance_all_align.finance_mapping_local` WHERE ingestionId='{ingestion_id}'"""

    mapping_local = (pandas_gbq.read_gbq(query, project_id=GCP_PROJECT, dialect='standard', ))
    print(mapping_local.columns)
    print(mapping_local[['level0']].head())

    # Nettoyage des colonnes (équivalent de UPPER(TRIM(...)))
    df['ingestionId_clean'] = df['ingestionId'].str.strip().str.upper()
    df['accountCostCenterCode'] = df['accountId'] + '.' + df['costCode']

    mapping_local['ingestionId_clean'] = mapping_local['ingestionId'].str.strip().str.upper()

    # Première jointure (cas général ledger avec accountCostCenterCode non vide et non null)
    mapping_local_filtered = mapping_local[
        (mapping_local['accountCostCenterCode'].notnull()) &
        (mapping_local['accountCostCenterCode'] != "")
        ]

    result_case1 = pd.merge(
        df,
        mapping_local_filtered,
        how='left',
        left_on=['ingestionId_clean', 'accountCostCenterCode'],
        right_on=['ingestionId_clean', 'accountCostCenterCode']
    )

    # Deuxième jointure (cas général avec accountCode mais sans accountCostCenterCode ou vide/null)
    mapping_local_null_or_empty = mapping_local[
        (mapping_local['accountCostCenterCode'].isnull()) |
        (mapping_local['accountCostCenterCode'] == "")
        ]

    result_case2 = pd.merge(
        df,
        mapping_local_null_or_empty,
        how='left',
        left_on=['ingestionId_clean', 'accountId'],
        right_on=['ingestionId_clean', 'accountCode']
    )

    # Combinez les résultats si nécessaire (par exemple, en choisissant le plus pertinent ou en concaténant)
    final_result = pd.concat([result_case1, result_case2], ignore_index=True)

    # Si des KPI sont calculés à partir du résultat final
    kpis["general_ledger_kpi"] = df_to_array(gl(final_result))

    return kpis


def finance_customer_kpis(file):
    def format_amount(amount):
        return f"{amount:,.0f}".replace(",", " ")

    def get_top_customers(df, category, top_n=5):
        """Get top customers for a given category."""
        tab = (df[df['clientCategory'].astype(str).str.upper() == category]
               .groupby('clientName', as_index=False)
               .agg(amountSum=('amountValue', lambda x: round(x.sum(), 2)))
               .assign(amountSum=lambda df: df['amountSum'].abs())
               .sort_values(by='amountSum', ascending=False)
               .head(top_n))[['clientName', 'amountSum']]
        tab['amountSum'] = tab['amountSum'].apply(format_amount)
        return df_to_array(tab)

    df = pd.read_parquet(file)

    kpis = {}

    kpis["customer_kpi"] = [["amountValue"], [format_amount(df['amountValue'].sum())]]
    kpis["customer_top_five_non_airlines"] = get_top_customers(df, 'NON AIRLINES')
    kpis["customer_top_five_airlines"] = get_top_customers(df, 'AIRLINES')

    return kpis


def finance_procurement_kpis(file):
    def format_amount(amount):
        return f"{amount:,.0f}".replace(",", " ")

    def get_top_supplierName(df, top_n=5):
        """Get top customers for a given category."""
        tab = (df
               .groupby('supplierName', as_index=False)
               .agg(amountSum=('amountValue', lambda x: round(x.sum(), 2)))
               .assign(amountSum=lambda df: df['amountSum'].abs())
               .sort_values(by='amountSum', ascending=False)
               .head(top_n))[['supplierName', 'amountSum']]
        tab['amountSum'] = tab['amountSum'].apply(format_amount)
        return df_to_array(tab)

    df = pd.read_parquet(file)

    kpis = {}

    kpis["procurement_kpi"] = [["amountValue"], [format_amount(df['amountValue'].sum())]]
    kpis["procurement_top_five"] = get_top_supplierName(df)

    return kpis


def finance_provisions_kpis(file):
    def format_amount(amount):
        return f"{amount:,.0f}".replace(",", " ")

    def get_top_customerName(df, top_n=5):
        """Get top customers for a given category."""
        tab = (df
               .groupby('customerName', as_index=False)
               .agg(amountSum=('amountValue', lambda x: round(x.sum(), 2)))
               .assign(amountSum=lambda df: df['amountSum'].abs())
               .sort_values(by='amountSum', ascending=False)
               .head(top_n))[['customerName', 'amountSum']]
        tab['amountSum'] = tab['amountSum'].apply(format_amount)
        return df_to_array(tab)

    df = pd.read_parquet(file)

    kpis = {}

    kpis["provisions_kpi"] = [["amountValue"],
                              [format_amount(df['amountValue'].sum())]]
    kpis["provisions_top_five"] = get_top_customerName(df)
    return kpis


import pandas as pd
from datetime import datetime


def format_amount(amount):
    return f"{amount:,.0f}".replace(",", " ")


def capex(df):
    # Étape 1 : Calcul du max_month
    max_month = (
        df.groupby(['extractYear'], as_index=False)
        .agg({'extractMonth': 'max'})
    )
    max_month['max_extractMonth'] = max_month['extractMonth']

    # Étape 2 : Calcul du YTD
    ytd = (
        df.groupby(['extractMonth', 'extractYear'], as_index=False)
        .agg({'amountSpentCY': 'sum'})
    )
    ytd['amountSum'] = ytd['amountSpentCY'].round(2)
    ytd['category'] = 'Total CAPEX spent on current year'
    ytd['job_datetime'] = datetime.now()

    # Étape 3 : Calcul du Monthly CAPEX
    monthly_capex = (
        df.groupby(['extractMonth', 'extractYear'], as_index=False)
        .agg({'amountSpentMonth': 'sum'})
    )
    monthly_capex['amountSum'] = monthly_capex['amountSpentMonth'].round(2)
    monthly_capex['category'] = 'Monthly CAPEX spent'
    monthly_capex['job_datetime'] = datetime.now()

    # Étape 4 : Jointure entre YTD et max_month
    ytd = ytd.merge(
        max_month,
        on=['extractMonth'],
        how='left',
        suffixes=('', '_max')
    )
    ytd = ytd[ytd['max_extractMonth'].notna()]

    # Étape 5 : Union des résultats
    final_result = pd.concat([monthly_capex, ytd], ignore_index=True)

    # Sélection des colonnes
    final_result = final_result[
        ["category", "extractMonth", "amountSum"]
    ]
    final_result['amountSum'] = final_result['amountSum'].apply(format_amount)

    return final_result


def finance_capex_kpis(file):
    def get_top_projectName(df, top_n=5):
        """Get top customers for a given category."""
        tab = (df
               .groupby('projectName', as_index=False)
               .agg(amountSum=('amountSpentMonth', lambda x: round(x.sum(), 2)))
               .assign(amountSum=lambda df: df['amountSum'].abs())
               .sort_values(by='amountSum', ascending=False)
               .head(top_n))[['projectName', 'amountSum']]
        tab['amountSum'] = tab['amountSum'].apply(format_amount)
        return df_to_array(tab)

    df = pd.read_parquet(file)
    df['extractDate'] = pd.to_datetime(df['extractDate'])
    df['extractYear'] = df['extractDate'].dt.year
    df['extractMonth'] = df['extractDate'].dt.month

    kpis = {}
    kpis["capex_kpi"] = df_to_array(capex(df))
    kpis["capex_top_five"] = get_top_projectName(df)
    return kpis


kpis_function_tab: Dict[FinanceFileTypes, Callable[[str], dict]] = {
    FinanceFileTypes.FINANCE_DEPOSITS: finance_deposits_kpis,  # OK
    FinanceFileTypes.FINANCE_GUARANTEES: finance_guarantees_kpis,  # OK
    FinanceFileTypes.FINANCE_CAPEX_FORECAST: finance_capex_forecast_kpis,  # CHECK CPX FILES ERROR
    FinanceFileTypes.FINANCE_RECEIVABLES: finance_receivables_kpis,  # OK
    FinanceFileTypes.FINANCE_CUSTOMER_REVENUES: finance_customer_kpis,
    FinanceFileTypes.FINANCE_PROCUREMENTS: finance_procurement_kpis,  # OK
    FinanceFileTypes.FINANCE_PROVISIONS: finance_provisions_kpis,  # AERODOM TO TEST
    FinanceFileTypes.FINANCE_CAPEX: finance_capex_kpis,  # OK
    FinanceFileTypes.FINANCE_GENERAL_LEDGER: finance_general_ledger_kpis  # OK
    # "CAPEX_DETAILED":,
    # "CAPEX_FORECAST_LONGTERM":,
    # "REF_CAPEX_PROJECTS":,
    # "BUDGET":,
}
