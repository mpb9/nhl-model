from math import e
import re
import pandas as pd
import numpy as np

from src.utility.structure import organize, reorder_col, shift_col
from src.utility.constants import NHL_TEAMS

# Purpose: Common Operations Pertaining Particularly to My Bizarre Needs & Desires


# info: Add a _TARGET column to the DataFrame
def add_known_col(df, col_name):
    if col_name in df.columns:
        col = df.groupby("team", group_keys=False).apply(
            lambda x: shift_col(x, col_name)
        )
        df[f"target_{col_name}"] = col
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


# info: Add the amount of rest to the DataFrame
# ! Add opponent rest??
def add_rest(df):
    df_rest = pd.DataFrame()
    s_to_h = 1 / 3600
    for season in df["season"].unique():
        for team in df["team"].unique():
            df_temp = organize(
                df[((df["season"] == season) & (df["team"] == team))].copy()
            )
            df_temp["date_time"] = pd.to_datetime(
                df_temp["game_date"] + " " + df_temp["game_time"]
            )
            df_temp.insert(17, "rest", np.nan)

            for index in range(1, len(df_temp)):
                df_temp.loc[index, "rest"] = (
                    s_to_h
                    * (
                        df_temp.loc[index, "date_time"]
                        - df_temp.loc[(index - 1), "date_time"]
                    ).total_seconds()
                )

            df_rest = pd.concat([df_rest, df_temp], ignore_index=True)
    df_rest.drop("date_time", axis=1, inplace=True)
    return organize(df_rest)


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


# info: Formats DF in my tidy format
def tidy_up(df):
    df = reorder_col(df.copy(), "game_id", 0)
    df = reorder_col(df.copy(), "team", 1)
    df = reorder_col(df.copy(), "opp_team", 2)
    df = reorder_col(df.copy(), "season", 3)
    df = reorder_col(df.copy(), "game_number", 4)
    df = reorder_col(df.copy(), "next_game_id", 5)
    df = reorder_col(df.copy(), "score", 6)
    df = reorder_col(df.copy(), "opp_score", 7)
    df = reorder_col(df.copy(), "win", 8)
    df = reorder_col(df.copy(), "reg_win", 9)
    df = reorder_col(df.copy(), "overtime", 10)
    df = reorder_col(df.copy(), "odds", 11)
    df = reorder_col(df.copy(), "opp_odds", 12)
    df = reorder_col(df.copy(), "ot_odds", 13)
    df = reorder_col(df.copy(), "situation", 14)
    df = reorder_col(df.copy(), "game_date", 15)
    df = reorder_col(df.copy(), "game_time", 16)
    df = reorder_col(df.copy(), "rest", 17)
    df = reorder_col(df.copy(), "is_home", 18)
    df = reorder_col(df.copy(), "iceTime", 19)
    return organize(df)


# info: Put Team Names in correct format
def format_team_name(name):
    for team in NHL_TEAMS:
        if name in team[1] or team[3] in name:
            return team[0]
        elif "N.J" in name or "NJ" in name:
            return "NJD"
        elif "S.J" in name or "SJ" in name:
            return "SJS"
        elif "L.A" in name or "LA" in name:
            return "LAK"
        elif "T.B" in name or "TB" in name:
            return "TBL"
        elif "St. Louis" in name:
            return "STL"
    return name


# info: Put Odds in correct format
def format_odds(df, odd_col, odd_type):
    if odd_type == "american":
        df[odd_col] = df[odd_col].apply(
            lambda x: (100 / (x + 100)) if x > 0 else ((-1 * x) / ((-1 * x) + 100))
        )
        return df.copy()
    elif odd_type == "decimal":
        df[odd_col] = df[odd_col].apply(lambda x: (1 / x))
        return df.copy()
    elif odd_type == "fractional":
        df[odd_col] = df[odd_col].apply(
            lambda x: (1 / (x.split("/")[0] / x.split("/")[1]) + 1)
        )
        return df.copy()
    return df.copy()


def gp_2019(team):
    if (
        "BOS" in team
        or "TBL" in team
        or "TOR" in team
        or "COL" in team
        or "CHI" in team
        or "CBJ" in team
        or "NYR" in team
        or "CGY" in team
        or "ARI" in team
        or "LAK" in team
        or "SJS" in team
    ):
        return 70
    elif (
        "MTL" in team
        or "OTT" in team
        or "DET" in team
        or "STL" in team
        or "WPG" in team
        or "VGK" in team
        or "EDM" in team
        or "ANA" in team
    ):
        return 71
    elif "CAR" in team or "NYI" in team:
        return 68
    else:
        return 69
