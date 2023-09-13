import pandas as pd

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.utility.math import *

from src.constants import *

from src.avgs import *

# Purpose: DIFFERENCE BETWEEN (RECENT DATA) & (LARGER SAMPLE)
# ! need to make sure each new row INCLUDES that row's game_id's info


# info: get difference between recent and past averages
def trajectory(
    df, recent_num, past_num, add_objs=["season", "game_number"], suffix=False
):
    df_recent = rolling_avgs(
        df.copy(), recent_num, include_null_next=False, suffix=False
    )
    df_past = rolling_avgs(df.copy(), past_num, include_null_next=False, suffix=False)

    obj_cols = list(df_recent.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df_recent.columns if col not in obj_cols]

    df_obj = df_recent[obj_cols].copy()
    df_data = df_recent[data_cols].copy() - df_past[data_cols].copy()

    if suffix:
        for col in data_cols:
            df_data = rename_col(df_data, col, f"{col}_{recent_num}v{past_num}")
    return drop_nulls(pd.concat([df_obj.copy(), df_data.copy()], axis=1))


# info: get difference between recent and season averages
def trajectory_season(df, recent_num, add_objs=["season", "game_number"], suffix=False):
    df_recent = rolling_avgs(df.copy(), recent_num, False, False)
    df_season = season_avgs(df.copy(), False)

    obj_cols = list(df_season.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df_season.columns if col not in obj_cols]

    df_obj = df_season[obj_cols].copy()
    df_data = df_recent[data_cols].copy() - df_season[data_cols].copy()

    if suffix:
        for col in data_cols:
            df_data = rename_col(df_data, col, f"{col}_{recent_num}vSZN")

    return drop_on_game_number(
        drop_nulls(pd.concat([df_obj.copy(), df_data.copy()], axis=1)), recent_num
    )


# info: get difference between two rolling/season avg DataFrames
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

    if is_season:
        return drop_on_game_number(
            drop_nulls(pd.concat([df_obj.copy(), df_data.copy()], axis=1)), rec_num
        )
    return drop_nulls(pd.concat([df_obj.copy(), df_data.copy()], axis=1))


# info: get linear regression of trajectory for previous X games
# includes the current game's data (:
def trajectory_linear(df, num_games, add_objs=["season", "game_number"], suffix=False):
    df_b0 = pd.DataFrame()
    df_b1 = pd.DataFrame()

    obj_cols = list(df.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df.columns if col not in obj_cols]
    x = list(range(0, num_games))

    for season in df["season"].unique():
        for team in df["team"].unique():
            group = organize(
                df[((df["season"] == season) & (df["team"] == team))].copy()
            )

            df_objs = group[obj_cols].copy()
            df_data = group[data_cols].copy()

            # Set df_b0 and df_b1 data_col values to NaN where game_number < num_games
            group.loc[(group["game_number"] < num_games), data_cols] = np.nan
            df_b0 = pd.concat([df_b0, group.iloc[0 : num_games - 1]], ignore_index=True)
            df_b1 = pd.concat([df_b1, group.iloc[0 : num_games - 1]], ignore_index=True)
            group = group.loc[group["game_number"] >= num_games]

            # Retrieve Linear Coefficients for each game
            for game in range(num_games, len(group) + 1):
                B = linear_coefs_grouped(x, df_data.loc[game - num_games : game - 1])
                df_b0 = pd.concat(
                    [df_b0, pd.concat([df_objs.loc[game - 1], B.iloc[0]], axis=0)],
                    ignore_index=True,
                )
                df_b1 = pd.concat(
                    [df_b1, pd.concat([df_objs.loc[game - 1], B.iloc[1]], axis=0)],
                    ignore_index=True,
                )
    if suffix:
        for col in data_cols:
            df_b0 = rename_col(df_b0, col, f"{col}_{num_games}_b0")
            df_b1 = rename_col(df_b1, col, f"{col}_{num_games}_b1")
    return [organize(df_b0), organize(df_b1)]
