import pandas as pd

from .personal import *
from .constants import *

# Purpose: Common Data Retrieval & Export Operations


# info: Exporting Stuff
def export_csv(df, szn, sit, name="", subfol="", pretty=True):
    if pretty:
        df = pretty_df(df)
    df.to_csv(
        CSV_DB_PATH
        + f"{szn}{'' if len(subfol)<1 else f'/{subfol}'}/{'' if len(name)<1 else f'{name}_'}{sit}{'' if szn == 'all' else f'_{szn}'}.csv",
        header=True,
        index=False,
    )
    return


def export_csv_no_nulls(df, szn, sit, name="", subfol="", pretty=True):
    if pretty:
        df = pretty_df(df)
    df = drop_nulls(df)
    df.to_csv(
        CSV_DB_PATH
        + f"{szn}{'' if len(subfol)<1 else f'/{subfol}'}/{'' if len(name)<1 else f'{name}_'}{sit}{'' if szn == 'all' else f'_{szn}'}.csv",
        header=True,
        index=False,
    )
    return


def export_csv_custom(df, szn, name, drop_nulls=True, pretty=True):
    if pretty:
        df = pretty_df(df)
    if drop_nulls:
        df = drop_nulls(df)
    df.to_csv(
        CSV_DB_PATH + f"{szn}/{name}.csv",
        header=True,
        index=False,
    )
    return


def export_csv_test(df, szn, sit, name="", pretty=True):
    if pretty:
        df = pretty_df(df)
    df.to_csv(
        CSV_DB_PATH
        + f"test/{'' if len(name)<1 else f'{name}_'}{sit}{'' if szn == 'all' else f'_{szn}'}.csv",
        header=True,
        index=False,
    )
    return


# info: Retrieving Stuff
def retrieve_csv(szn, sit, name="", subfol=""):
    return pd.read_csv(
        CSV_DB_PATH
        + f"{szn}{'' if len(subfol)<1 else f'/{subfol}'}/{'' if len(name)<1 else f'{name}_'}{sit}{'' if szn == 'all' else f'_{szn}'}.csv",
    )


def primary_csv(season="all", situation="5on5"):
    return pd.read_csv(
        CSV_DB_PATH
        + f"{season}/{situation}{'' if season == 'all' else f'_{season}'}.csv"
    )


# info: Access Utilty CSVs
def get_special_columns():
    return pd.read_csv(CSV_DB_PATH + "utils/special_columns.csv")


def get_NHL_teams():
    return pd.read_csv(CSV_DB_PATH + "utils/teams.csv")


def get_seasons():
    return pd.read_csv(CSV_DB_PATH + "utils/seasons.csv")
