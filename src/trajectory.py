import pandas as pd

from src.utility import *
from src.constants import *
from src.avgs import *

# Purpose: DIFFERENCE BETWEEN (RECENT DATA) & (LARGER SAMPLE)


# info: get difference between recent and past averages
def trajectory(
    df, recent_num, past_num, add_objs=["season", "game_number"], suffix=True
):
    df_recent = rolling_avgs(df.copy(), recent_num, False, False)
    df_past = rolling_avgs(df.copy(), past_num, False, False)

    obj_cols = list(df_recent.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df_recent.columns if col not in obj_cols]

    df_obj = df_recent[obj_cols].copy()
    df_data = df_recent[data_cols].copy() - df_past[data_cols].copy()

    if suffix:
        for col in data_cols:
            df_data = rename_col(df_data, col, f"{col}_{recent_num}v{past_num}")
    return organize(pd.concat([df_obj.copy(), df_data.copy()], axis=1))


# info: get difference between recent and season averages
def trajectory_season(df, recent_num, add_objs=["season", "game_number"], suffix=True):
    df_recent = rolling_avgs(df.copy(), recent_num, False, False)
    df_season = season_avgs(df.copy(), False)

    obj_cols = list(df_season.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df_season.columns if col not in obj_cols]

    df_obj = df_season[obj_cols].copy()
    df_data = df_recent[data_cols].copy() - df_season[data_cols].copy()

    if suffix:
        for col in data_cols:
            df_data = rename_col(df_data, col, f"{col}_{recent_num}vSZN")

    return organize(pd.concat([df_obj.copy(), df_data.copy()], axis=1))


def trajectory_quick(
    recent_df,
    past_df,
    rec_num,
    past_num,
    is_season=False,
    add_objs=["season", "game_number"],
    suffix=False,
):
    obj_cols = list(recent_df.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in recent_df.columns if col not in obj_cols]

    df_obj = recent_df[obj_cols].copy()
    df_data = recent_df[data_cols].copy() - past_df[data_cols].copy()

    if suffix:
        for col in data_cols:
            if is_season:
                df_data = rename_col(df_data, col, f"{col}_{rec_num}vSZN")
            else:
                df_data = rename_col(df_data, col, f"{col}_{rec_num}v{past_num}")

    return organize(pd.concat([df_obj.copy(), df_data.copy()], axis=1))
