import pandas as pd
from .constants import *


# info: Row Operations
def orderby_id(df, col_name="game_id"):
    df = df.sort_values(by=col_name, ascending=True)
    df.reset_index(drop=True, inplace=True)
    return df


def orderby_mult(df, col_name_1="game_id", col_name_2="team"):
    df = df.sort_values(by=[col_name_1, col_name_2], ascending=[True, True])
    df.reset_index(drop=True, inplace=True)
    return df


# info: Column Operations
def shift_col(team, col_name, shift=-1):
    next_col = team[col_name].shift(shift)
    return next_col


def reorder_col(df, col_name, new_index):
    column_to_move = df[col_name]
    df = df.drop(columns=col_name)
    df.insert(new_index, col_name, column_to_move)
    return df


def rename_col(df, col_name, new_col_name):
    df.rename(columns={col_name: new_col_name}, inplace=True)
    return df


def add_next_col(df, col_name):
    col = df.groupby("team", group_keys=False).apply(lambda x: shift_col(x, col_name))
    df[f"next_{col_name}"] = col
    return orderby_id(df.copy())


# info: Combine Data
def concat_df(dfs, ax=1):
    df_new = pd.DataFrame(dfs[0])
    for df in dfs[1:]:
        df_new = pd.concat([df_new.copy(), df], axis=ax)
    df_new = df_new.dropna()
    return orderby_id(df_new.copy())


def merge_df(dfs, on_col="game_id"):
    df_new = pd.DataFrame(dfs[0])
    for df in dfs[1:]:
        df_new = pd.merge(df_new, pd.DataFrame(df), on=on_col)
    return df_new


def merge_opp_data(df, common_cols, team_x, team_y, on_col):
    df = df.merge(
        df[common_cols + [team_x, team_y, on_col]],
        left_on=[team_x, on_col],
        right_on=[team_y, on_col],
        suffixes=("_x", "_y"),
    )
    return orderby_id(df.copy())


# info: Access Data


def get_special_columns():
    return pd.read_csv(CSV_DB_PATH + "utils/special_columns.csv")
