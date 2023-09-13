import pandas as pd
import numpy as np

from .structure import *
from ..constants import *

# Purpose: Common Operations Pertaining Particularly to My Bizarre Needs & Desires


# info: Add a _NEXT column to the DataFrame
def add_next_col(df, col_name):
    col = df.groupby("team", group_keys=False).apply(lambda x: shift_col(x, col_name))
    df[f"next_{col_name}"] = col
    return organize(df)


# info: Add the game_number column to the DataFrame
def add_game_number(df):
    df_game_num = pd.DataFrame()
    for season in df["season"].unique():
        for team in df["team"].unique():
            df_temp = organize(df[((df["season"] == season) & (df["team"] == team))])
            df_temp.insert(4, "game_number", list(range(1, len(df_temp) + 1)))
            df_game_num = pd.concat([df_game_num, df_temp], ignore_index=True)
    df_game_num["game_number"] = df_game_num["game_number"].astype(int)
    return organize(df_game_num)


# info: Fills all null next_game_id values with "NA"
def fill_null_next(df):
    df["next_game_id"].fillna("NA", inplace=True)
    return organize(df)


# info: Drop rows with null values (default: not including where next_game_id is NULL)
def drop_nulls(df, fill_NA=True, keep_NA=False):
    df = fill_null_next(df).dropna() if fill_NA else organize(df.dropna())
    df["next_game_id"] = (
        df["next_game_id"].replace("NA", np.nan) if not keep_NA else df["next_game_id"]
    )
    return organize(df)


# info: Drop rows where game_number = num
def drop_on_game_number(df, num):
    df = df[df.game_number != num]
    return organize(df)


# info: Merge opponent's data into each row of the DataFrame
def merge_opp_data(df, common_cols, team_x, team_y, on_col):
    df = df.merge(
        df[common_cols + [team_x, team_y, on_col]],
        left_on=[team_x, on_col],
        right_on=[team_y, on_col],
        suffixes=("_x", "_y"),
    )
    return organize(df)
