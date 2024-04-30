import numpy as np
import pandas as pd

from src.utility.structure import *
from src.utility.storage import *
from src.utility.personal import *
from src.utility.constants import *

# Purpose: Add Season Odds Data to the DataFrame (from www.sportsoddshistory.com)
# ! ADD STANLEY CUP ODDS... SPECIFIED BY DATE (1-5 DAYS DURING EACH SEASON)


# info: Load Point Total Odds
# initial cols: Team, Point Total, Over Odds, Under Odds, Actual Points, Result
# final cols: team, pts_exp, pts_over_odds, pts_under_odds, pts_szn, pts_szn_over_exp, season
def update_points_odds(year, export=False):
    df_szn = pd.read_csv(
        CSV_DB_PATH + f"season_odds/point_total_odds_TEMP.csv",
    )

    df_szn = rename_col(df_szn, "Team", "team")
    df_szn = rename_col(df_szn, "Point Total", "pts_exp")
    df_szn = rename_col(df_szn, "Over Odds", "pts_over_odds")
    df_szn = rename_col(df_szn, "Under Odds", "pts_under_odds")
    df_szn = rename_col(df_szn, "Actual Points", "pts_szn")
    df_szn = rename_col(df_szn, "Result", "pts_szn_over_exp")
    df_szn["season"] = year

    exp_games = 82 if year != 2020 else 56
    if year == 2012:
        exp_games = 48

    for index, row in df_szn.iterrows():
        df_szn.at[index, "team"] = format_team_name(row["team"])
        if year != 2019:
            df_szn.at[index, "pts_szn"] = row["pts_szn"] / exp_games
        else:
            df_szn.at[index, "pts_szn"] = row["pts_szn"] / gp_2019(row["team"])

    df_szn["pts_exp"] = df_szn["pts_exp"] / exp_games
    df_szn["pts_szn_over_exp"] = df_szn["pts_szn"] - df_szn["pts_exp"]

    df_szn = format_odds(df_szn, "pts_over_odds", "american")
    df_szn = format_odds(df_szn, "pts_under_odds", "american")

    df = pd.concat(
        [
            pd.read_csv(
                CSV_DB_PATH + "season_odds/point_total_odds.csv",
            ),
            df_szn,
        ],
        ignore_index=True,
    )

    df = reorder_col(df.copy(), "team", 0)
    df = reorder_col(df.copy(), "season", 1)
    df = reorder_col(df.copy(), "pts_exp", 2)
    df = reorder_col(df.copy(), "pts_szn", 3)
    df = reorder_col(df.copy(), "pts_szn_over_exp", 4)
    df = reorder_col(df.copy(), "pts_over_odds", 5)
    df = reorder_col(df.copy(), "pts_under_odds", 6)

    df = orderby_mult(df, col_name_1="season", col_name_2="team")

    if export:
        df.to_csv(
            CSV_DB_PATH + "season_odds/point_total_odds.csv",
            header=True,
            index=False,
        )
    return df.copy()


# info: Load Playoff Odds
# initial cols: Team, Make Odds, Miss Odds, Result
# final cols: team, playoff_make_odds, playoff_miss_odds, playoff_made, season
def update_playoff_odds(year, export=False):
    df_szn = pd.read_csv(
        CSV_DB_PATH + f"season_odds/playoff_odds_TEMP.csv",
    )

    df_szn = rename_col(df_szn, "Team", "team")
    df_szn = rename_col(df_szn, "Make Odds", "playoff_make_odds")
    df_szn = rename_col(df_szn, "Miss Odds", "playoff_miss_odds")
    df_szn = rename_col(df_szn, "Result", "playoff_made")

    df_szn["season"] = year

    for index, row in df_szn.iterrows():
        df_szn.at[index, "team"] = format_team_name(row["team"])

        if row["playoff_made"] == "MAKE":
            df_szn.at[index, "playoff_made"] = 1
        elif row["playoff_made"] == "MISS":
            df_szn.at[index, "playoff_made"] = 0

    df_szn = format_odds(df_szn, "playoff_make_odds", "american")
    df_szn = format_odds(df_szn, "playoff_miss_odds", "american")

    df = pd.concat(
        [
            pd.read_csv(
                CSV_DB_PATH + "season_odds/playoff_odds.csv",
            ),
            df_szn,
        ],
        ignore_index=True,
    )

    df = reorder_col(df.copy(), "team", 0)
    df = reorder_col(df.copy(), "season", 1)
    df = reorder_col(df.copy(), "playoff_make_odds", 2)
    df = reorder_col(df.copy(), "playoff_miss_odds", 3)
    df = reorder_col(df.copy(), "playoff_made", 4)

    df = orderby_mult(df, col_name_1="season", col_name_2="team")

    if export:
        df.to_csv(
            CSV_DB_PATH + "season_odds/playoff_odds.csv",
            header=True,
            index=False,
        )
    return df.copy()


# info: Load Stanley Cup Odds
# ! ADD STANLEY CUP ODDS... SPECIFIED BY DATE (1-5 DAYS DURING EACH SEASON)
