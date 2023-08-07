import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

sys.path.append("/get_data")
from .get_data.nhl_data import NHLData
from .get_data.utility_data import UtilityData
from .utility import *


class PerGameData:
    def __init__(self):
        self.nhl_data = NHLData()
        self.utility_data = UtilityData()

    def next_game_ids_DF(self, df):
        df = orderby_id(df)
        for index, row in df.iterrows():
            next_game_id_home = "NA"
            for i in range(index + 1, len(df)):
                if df.loc[i, "season"] != row["season"]:
                    next_game_id_away = "NA NEW_SZN"
                    break
                if (
                    df.loc[i, "home_team"] == row["home_team"]
                    or df.loc[i, "away_team"] == row["home_team"]
                ):
                    next_game_id_home = df.loc[i, "game_id"]
                if next_game_id_home == df.loc[i, "game_id"]:
                    break
            df.loc[index, "next_game_id_home"] = next_game_id_home

        for index, row in df.iterrows():
            next_game_id_away = "NA"
            for i in range(index + 1, len(df)):
                if df.loc[i, "season"] != row["season"]:
                    next_game_id_away = "NA NEW_SZN"
                    break
                if (
                    df.loc[i, "home_team"] == row["away_team"]
                    or df.loc[i, "away_team"] == row["away_team"]
                ):
                    next_game_id_away = df.loc[i, "game_id"]
                if next_game_id_away == df.loc[i, "game_id"]:
                    break
            df.loc[index, "next_game_id_away"] = next_game_id_away

        return df

    def by_team(self, df_1, df_2):
        df_1 = self.by_team_away(df_1)
        df_2 = self.by_team_home(df_2)
        df = pd.concat([df_1, df_2], axis=0)
        df = rename_col(df, "score", "final_score")
        df = rename_col(df, "opp_score", "opp_final_score")
        for index, row in df.iterrows():
            if row["result"] == 1:
                win = 1
                overtime = 0
            elif row["result"] == 0 and row["opp_result"] == 0:
                win = 0
                overtime = 0
            else:
                win = 0
                overtime = 1
            df.loc[index, "win"] = win
            df.loc[index, "overtime"] = overtime
        df = df.drop(columns=["result", "opp_result", "ot_result"])
        df = df.drop("opp_next_game_id", axis=1)
        df = self.reorder_by_team_columns(df)
        return orderby_id(df)

    def by_team_away(self, df):
        columns = df.columns
        other_columns = []
        new_columns = []
        new_data = []

        for column in columns:
            away_col = (
                column.replace("away_", "").replace("_away", "").replace("Away", "")
            )
            away_col = away_col.replace("home_", "opp_")
            if "_home" in away_col:
                away_col = "opp_" + away_col.replace("_home", "")
            elif "Home" in away_col:
                away_col = "opp_" + away_col.replace("Home", "")

            if away_col not in other_columns:
                new_columns.append(away_col)
                new_data.append(df[column])

        away_df = pd.concat(new_data, axis=1, keys=new_columns)
        away_df["is_home"] = 0
        return orderby_id(away_df)

    def by_team_home(self, df):
        columns = df.columns
        other_columns = []
        new_columns = []
        new_data = []

        for column in columns:
            home_col = (
                column.replace("home_", "").replace("_home", "").replace("Home", "")
            )
            home_col = home_col.replace("away_", "opp_")
            if "_away" in home_col:
                home_col = "opp_" + home_col.replace("_away", "")
            elif "Away" in home_col:
                home_col = "opp_" + home_col.replace("Away", "")

            if home_col not in other_columns:
                new_columns.append(home_col)
                new_data.append(df[column])

        home_df = pd.concat(new_data, axis=1, keys=new_columns)
        home_df["is_home"] = 1
        return orderby_id(home_df)

    def reorder_by_team_columns(self, df):
        cols_2_move = [
            ["team", 1],
            ["opp_team", 2],
            ["final_score", 3],
            ["opp_final_score", 4],
            ["season", 5],
            ["game_date", 6],
            ["next_game_id", 7],
            ["is_home", 8],
            ["situation", 9],
            ["win", 10],
            ["overtime", 11],
            ["odds", 12],
            ["opp_odds", 13],
            ["ot_odds", 14],
        ]
        for col_movin in cols_2_move:
            column_to_move = df[col_movin[0]]
            df = df.drop(columns=col_movin[0])
            df.insert(col_movin[1], col_movin[0], column_to_move)
        return df

    def season_per_game_data(self, situation, season):
        season_condition = {"header": "season", "conditional": "=", "value": season}
        games = self.nhl_data.conditional_data("games", [season_condition])
        prev_game_ids = self.nhl_data.conditional_prev_game_ids([season_condition])
        odds_x_game = self.nhl_data.ref_table_conditional_data(
            "odds_x_game",
            "games",
            "game_id",
            [season_condition],
        )
        team_x_game = self.nhl_data.conditional_data(
            "team_x_game",
            [
                {"header": "situation", "conditional": "=", "value": situation},
                season_condition,
            ],
        )
        return merge_df([games, prev_game_ids, odds_x_game])
