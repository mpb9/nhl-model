from numpy import exp
import pandas as pd

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.utility.math import *
from src.utility.constants import *

from src.avgs import *

# Purpose: DIFFERENCE BETWEEN (RECENT DATA) & (LARGER SAMPLE)
# ! need to make sure each new row INCLUDES that row's game_id's info
# ! ADD SEASON_ODDS TRAJECTORIES (points, playoffs, stanley cup)


# info: get difference between recent and past averages
def trajectory(
    df,
    recent_num,
    past_num,
    add_objs=["season", "game_number", "is_home", "iceTime", "rest"],
    suffix=False,
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
def trajectory_season(
    df,
    recent_num,
    add_objs=["season", "game_number", "is_home", "iceTime", "rest"],
    suffix=False,
):
    df_recent = rolling_avgs(df.copy(), recent_num, False, False)
    df_season = season_avgs(df.copy(), False)

    obj_cols = list(df_season.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df_season.columns if col not in obj_cols]

    df_obj = df_season[obj_cols].copy()
    df_data = df_recent[data_cols].copy() - df_season[data_cols].copy()

    if suffix:
        for col in data_cols:
            df_data = rename_col(df_data, col, f"{col}_{recent_num}vSZN")

    # ! this might be ignoring the first rolling avg value.. check it out
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
    add_objs=["season", "game_number", "is_home", "iceTime", "rest"],
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

    # ! this might be ignoring the first rolling avg value.. check it out
    if is_season:
        return drop_on_game_number(
            drop_nulls(pd.concat([df_obj.copy(), df_data.copy()], axis=1)), rec_num
        )
    return drop_nulls(pd.concat([df_obj.copy(), df_data.copy()], axis=1))


# info: get linear regression of trajectory for previous X games
# includes the current game's data (:
def trajectory_linear(
    df,
    num_games,
    add_objs=["season", "game_number", "is_home", "iceTime", "rest"],
    suffix=False,
):
    b0 = df.iloc[:0].copy()
    b1 = df.iloc[:0].copy()

    obj_cols = list(df.select_dtypes(include=["object"]).columns) + add_objs
    data_cols = [col for col in df.columns if col not in obj_cols]
    x = np.array(list(range(0, num_games)))

    for season in df["season"].unique():
        for team in df["team"].unique():
            group = organize(
                df[((df["season"] == season) & (df["team"] == team))].copy()
            )
            df_objs = group[obj_cols].copy()
            df_data = group[data_cols].copy()

            for game_index in range(num_games - 1, len(group)):
                B = linear_coefs_grouped(
                    x.copy(),
                    df_data.loc[game_index - num_games + 1 : game_index].copy(),
                )
                B.insert(0, "game_number", [game_index + 1, game_index + 1])

                b0 = pd.concat(
                    [
                        b0.copy(),
                        df_objs[df_objs.game_number == game_index + 1].merge(
                            B.loc[:"b0"].copy(), on="game_number"
                        ),
                    ],
                    ignore_index=True,
                )

                b1 = pd.concat(
                    [
                        b1.copy(),
                        df_objs[df_objs.game_number == game_index + 1].merge(
                            B.loc["b1":].copy(), on="game_number"
                        ),
                    ],
                    ignore_index=True,
                )

    if suffix:
        for col in data_cols:
            b0 = rename_col(b0.copy(), col, f"{col}_{num_games}_b0")
            b1 = rename_col(b1.copy(), col, f"{col}_{num_games}_b1")
    return [organize(b0), organize(b1)]


# info: Load Season to Season Trajectory of Point Total Odds
# ! ADD TRAJECTORY OF POINT TOTAL ODDS FROM BEGINNING OF X SEASON TO CURRENT SEASON
def trajectory_points_exp_odds(sample_szns=3, suffix=False):
    df_szn = pd.read_csv(
        CSV_DB_PATH + f"season_odds/point_total_odds_TEMP.csv",
    )
    b0 = pd.DataFrame()
    b1 = pd.DataFrame()
    x = np.array(list(range(0, sample_szns)))

    for team in df_szn.team.unique():
        df_team = orderby_id(df_szn[df_szn.team == team].copy(), col_name="season")
        szn = df_team.season.iloc[0] + sample_szns - 1

        while szn <= df_team.season.iloc[len(df_team.season) - 1]:
            [exp_b0, exp_b1] = linear_coef(
                x.copy(),
                df_team[
                    ((df_team.season > szn - sample_szns) & (df_team.season <= szn))
                ].pts_exp.copy(),
                sample_szns,
            )
            b0 = pd.concat(
                [
                    b0.copy(),
                    pd.DataFrame(
                        {
                            "team": team,
                            "season": szn,
                            "pts_exp": exp_b0,
                        }
                    ),
                ],
                ignore_index=True,
            )
            b1 = pd.concat(
                [
                    b1.copy(),
                    pd.DataFrame(
                        {
                            "team": team,
                            "season": szn,
                            "pts_exp": exp_b1,
                        }
                    ),
                ],
                ignore_index=True,
            )
            szn += 1

    if suffix:
        b0 = rename_col(b0.copy(), "pts_exp", f"pts_exp_{sample_szns}_b0")
        b1 = rename_col(b1.copy(), "pts_exp", f"pts_exp_{sample_szns}_b1")

    return [orderby_mult(b0, "season", "team"), orderby_mult(b1, "season", "team")]


# info: Load Season to Season Trajectory of Playoff Odds
# ! ADD TRAJECTORY OF PLAYOFF ODDS FROM BEGINNING OF X SEASON TO CURRENT SEASON

# info: Load Season to Season Trajectory of Stanley Cup Odds
# ! ADD TRAJECTORY OF STANLEY CUP ODDS FROM BEGINNING OF X SEASON TO CURRENT SEASON

# info: Load In-Season Trajectory of Stanley Cup Odds
# ! ADD TRAJECTORY OF STANLEY CUP ODDS FROM START OF SEASON TO END OF SEASON
