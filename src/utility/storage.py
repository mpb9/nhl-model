import pandas as pd

from .personal import drop_nulls, tidy_up
from .constants import DB_PATH, CSV_DB_PATH, BY_TEAM_DB, UTILS_DB

# Purpose: Common Data Retrieval & Export Operations


# MARK: Export CSVs
def export_csv_builder(df, szn, sit, name="", subfol="", tidy=True):
    if tidy:
        df = tidy_up(df)
    df.to_csv(
        DB_PATH
        + f"{szn}{'' if not bool(subfol) else f'/{subfol}'}/{'' if not bool(name) else f'{name}_'}{sit}{'' if not bool(szn) else f'_{szn}'}.csv",
        header=True,
        index=False,
    )


def export_csv_no_nulls_builder(df, szn, sit, name="", subfol="", tidy=True):
    df = drop_nulls(df)
    export_csv_builder(df, szn, sit, name, subfol, tidy)


def export_csv_basic(df, szn, name, no_nulls=True, tidy=True):
    if tidy:
        df = tidy_up(df)
    if no_nulls:
        df = drop_nulls(df)
    df.to_csv(
        DB_PATH + f"{szn}/{name}.csv",
        header=True,
        index=False,
    )


def export_csv_test(df, szn, sit, name="", tidy=True):
    if tidy:
        df = tidy_up(df)
    df.to_csv(
        CSV_DB_PATH
        + f"test/{'' if len(name)<1 else f'{name}_'}{sit}{'' if szn == 'all' else f'_{szn}'}.csv",
        header=True,
        index=False,
    )


def export_path_builder(szn, sit, name="", subfol=""):
    return (
        DB_PATH
        + f"{szn}{'' if not bool(subfol) else f'/{subfol}'}/{'' if not bool(name) else f'{name}_'}{sit}{'' if not bool(szn) else f'_{szn}'}.csv"
    )


# MARK: Load CSVs
def load_csv(szn, sit, name="", subfol=""):
    return pd.read_csv(
        CSV_DB_PATH
        + f"{szn}{'' if not bool(subfol) else f'/{subfol}'}/{'' if not bool(name) else f'{name}_'}{sit}{'' if not bool(szn) else f'_{szn}'}.csv",
    )


def load_by_team_csv(season="", situation="5on5"):
    df = pd.read_csv(BY_TEAM_DB + f"/{situation}.csv")

    if not bool(season):
        return df

    else:
        if "-" in season:
            season_range = season.split("-")
            print(season_range)

            return df[
                (df["season"] >= season_range[0]) & (df["season"] <= season_range[1])
            ]

    return df[df["season"] == season]


# MARK: Load Utility CSVs
def get_special_columns():
    return pd.read_csv(UTILS_DB + "/special_columns.csv")


def get_NHL_teams():
    return pd.read_csv(UTILS_DB + "/teams.csv")


def get_seasons():
    return pd.read_csv(UTILS_DB + "/seasons.csv")
