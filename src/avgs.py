import pandas as pd

from src.utility import *
from src.constants import *

# Purpose: ROLLING AVERAGES FOR EACH TEAM OVER SPAN


def rolling_avgs(
    df,
    num_games,
    include_null_next=True,
    suffix=True,
    add_objs=["season", "game_number"],
):
    if include_null_next:
        df["next_game_id"].fillna("NA", inplace=True)

    obj_cols = list(df.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df.columns if col not in obj_cols]

    df = df.groupby(["team", "season"], group_keys=False).apply(
        team_avg_helper, obj_cols=obj_cols, data_cols=data_cols, num_games=num_games
    )
    if suffix:
        for col in data_cols:
            df = rename_col(df, col, f"{col}_{num_games}")

    return organize(df)


def team_avg_helper(group, obj_cols, data_cols, num_games):
    group = organize(group)
    roll_data = group[data_cols].copy()
    roll_data = roll_data.rolling(num_games).mean()

    return pd.concat([group[obj_cols].copy(), roll_data.copy()], axis=1)


def season_avgs(df, suffix=True, add_objs=["season", "game_number"]):
    df_SZN = pd.DataFrame()

    obj_cols = list(df.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df.columns if col not in obj_cols]

    for season in df["season"].unique():
        for team in df["team"].unique():
            df_data = organize(
                df[((df["season"] == season) & (df["team"] == team))].copy()
            )
            # df_data.insert(1, "game_number", list(range(1, len(df_data) + 1)))
            # df_data["game_number"] = df_data["game_number"].astype(int)

            df_objs = df_data[obj_cols].copy()
            df_data = df_data[data_cols].copy()

            # info: create rolling season averages
            for i in range(1, len(df_data)):
                df_data.loc[i] = (df_data.loc[i - 1] * i + df_data.loc[i]) / (i + 1)

            df_SZN = pd.concat(
                [df_SZN, pd.concat([df_objs, df_data], axis=1)],
                ignore_index=True,
            )
    if suffix:
        for col in data_cols:
            df_SZN = rename_col(df_SZN, col, f"{col}_SZN")

    return organize(df_SZN)
