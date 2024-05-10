import pandas as pd
from src.utility.constants import *

# Purpose: Common DataFrame Structural Operations


# info: Row Operations
def organize(df):
    df = df.sort_values(by=["game_id", "team"], ascending=[True, True])
    df.reset_index(drop=True, inplace=True)
    return df.copy()


def orderby_id(df, col_name="game_id"):
    df = df.sort_values(by=col_name, ascending=True)
    df.reset_index(drop=True, inplace=True)
    return df.copy()


def orderby_mult(df, col_name_1="game_id", col_name_2="team"):
    df = df.sort_values(by=[col_name_1, col_name_2], ascending=[True, True])
    df.reset_index(drop=True, inplace=True)
    return df.copy()


# info: Column Operations
def shift_col(team, col_name, shift=-1):
    return team[col_name].shift(shift)


def reorder_col(df, col_name, new_index):
    column_to_move = df[col_name]
    df = df.drop(columns=col_name)
    df.insert(new_index, col_name, column_to_move)
    return df.copy()


def rename_col(df, col_name, new_col_name):
    df.rename(columns={col_name: new_col_name}, inplace=True)
    return df.copy()


# info: Combine Data
def concat_df(dfs, ax=1):
    df_new = pd.DataFrame(dfs[0])
    for df in dfs[1:]:
        df_new = pd.concat([df_new.copy(), df], axis=ax)
    df_new = df_new.dropna()
    return organize(df_new)


def merge_df(dfs, on_col="game_id"):
    df_new = pd.DataFrame(dfs[0])
    for df in dfs[1:]:
        df_new = pd.merge(df_new, pd.DataFrame(df), on=on_col)
    return organize(df_new)
