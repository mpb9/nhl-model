import pandas as pd

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.utility.constants import *

# Purpose: Initialize and Update a Model Iteration


class NHLModel:
    def __init__(self, df, szn, sit, target):
        self.df = df.copy()
        self.szn = szn
        self.sit = sit
        self.target = target
        self.data = df.copy()
        self.x = pd.DataFrame()
        self.y = pd.Series()
        self.KNOWN_COLS = [
            "opp_team",
            "game_date",
            "game_time",
            "rest",
            "is_home",
            "odds",
            "opp_odds",
            "ot_odds",
        ]
        self.IGNORE_COLS = [
            "game_id",
            "team",
            "opp_team",
            "season",
            "game_number",
            "next_game_id",
            "game_date",
            "situation",
            "game_time",
            "target_opp_team",
            "target_game_date",
            "target_game_time",
        ]

    def prepare(self):
        # Add Target
        target_data = retrieve_csv("all", self.sit, "target", "")
        self.df["target"] = target_data[self.target].copy()
        if self.szn != "all":
            self.df["target"] = target_data[target_data.season == self.szn][
                self.target
            ].copy()

        # Add Target Game Known Data
        df_known = pd.DataFrame()
        for season in self.df["season"].unique():
            df_temp = organize(self.df[self.df.season == season].copy())
            for known in self.KNOWN_COLS:
                df_temp = add_known_col(df_temp, known)

            df_known = pd.concat([df_known, df_temp], ignore_index=True)

        self.df = organize(df_known)

        # Specify Model Relevant Data
        self.update_model_data()

        return

    def update_model_data(self):
        self.data = self.df[
            [col for col in self.df.columns if col not in self.IGNORE_COLS]
        ].copy()

        self.x = self.data.drop("target", axis=1).copy()
        self.y = self.data["target"].copy()

        return

    def drop_nulls(self):
        for col in self.data:
            self.data = self.data[~pd.isnull(self.data[col])]

        self.x = self.data.drop("target", axis=1).copy()
        self.y = self.data["target"].copy()

        return

    def add_power_rank(self, type="", num_days=0):
        return self.df.copy()

    def add_sos(self, type="imp", num_days=""):
        return self.df.copy()

    def add_home_ice(self, type="imp", num_days=""):
        return self.df.copy()

    def add_away_ice(self, type="imp", num_days=""):
        return self.df.copy()

    def add_trajectory(
        self,
        type="compare",
        recent_num=4,
        past_num=0,
        add_objs=["season", "game_number", "is_home", "iceTime", "rest"],
        suffix=False,
    ):
        if past_num == 0:
            print("SEASON")
        return self.df.copy()

    def add_rolling(
        self,
        num_games=0,
        add_objs=["season", "game_number", "is_home", "iceTime", "rest"],
        include_null_next=True,
        suffix=False,
    ):
        if num_games == 0:
            print("SEASON")
        return self.df.copy()

    def add_points_odds(self):
        df_pts = pd.read_csv(
            CSV_DB_PATH + "season_odds/point_total_odds.csv",
        )
        df_pts_TEMP = pd.DataFrame()

        for season in self.df["season"].unique():
            df_s = self.df[self.df.season == season].copy()
            for team in df_s["team"].unique():
                df_temp = organize(
                    self.df[
                        ((self.df["season"] == season) & (self.df["team"] == team))
                    ].copy()
                )
                pts = df_pts[(df_pts.season == season) & (df_pts.team == team)].copy()
                df_temp["pts_exp"] = pts["pts_exp"].iloc[0]
                # df_temp["pts_szn"] = pts["pts_szn"].iloc[0]
                # df_temp["pts_szn_over_exp"] = pts["pts_szn_over_exp"].iloc[0]
                df_temp["pts_over_odds"] = pts["pts_over_odds"].iloc[0]
                df_temp["pts_under_odds"] = pts["pts_under_odds"].iloc[0]

                df_pts_TEMP = pd.concat([df_pts_TEMP, df_temp], ignore_index=True)

        self.df = organize(df_pts_TEMP.copy())
        self.update_model_data()
        return

    def add_playoff_odds(self):
        df_po = pd.read_csv(
            CSV_DB_PATH + "season_odds/playoff_odds.csv",
        )
        df_po_TEMP = pd.DataFrame()

        for season in self.df["season"].unique():
            df_s = self.df[self.df.season == season].copy()
            for team in df_s["team"].unique():
                df_temp = organize(
                    self.df[
                        ((self.df["season"] == season) & (self.df["team"] == team))
                    ].copy()
                )
                po = df_po[(df_po.season == season) & (df_po.team == team)].copy()
                df_temp["playoff_make_odds"] = po["playoff_make_odds"].iloc[0]
                df_temp["playoff_miss_odds"] = po["playoff_miss_odds"].iloc[0]
                # df_temp["playoff_made"] = po["playoff_made"].iloc[0]

                df_po_TEMP = pd.concat([df_po_TEMP, df_temp], ignore_index=True)

        self.df = organize(df_po_TEMP.copy())
        self.update_model_data()
        return
