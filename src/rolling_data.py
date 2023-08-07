import pandas as pd

from src.utility import *
from src.constants import *


class RollingData:
    def __init__(
        self,
        df,
        selected_cols,
        num_games,
        include_null_next=True,
        groupby_cols=["team", "season"],
    ):
        self.cols = []
        self.num_games = num_games
        self.essentials = pd.DataFrame()
        self.df = self.init_rolling_data(
            df, selected_cols, num_games, include_null_next, groupby_cols
        )

    def init_rolling_data(
        self,
        df,
        selected_cols,
        num_games,
        include_null_next=True,
        groupby_cols=["team", "season"],
    ):
        if include_null_next:
            df["next_game_id"].fillna("NA", inplace=True)
        self.num_games = num_games
        self.df = df[groupby_cols + list(selected_cols)]
        self.df = self.df.groupby(groupby_cols, group_keys=False).apply(
            self.find_team_averages, num_games=num_games
        )
        self.cols = [f"{col}_{num_games}" for col in self.df.columns]
        self.df.columns = self.cols
        self.essentials = self.get_essentials(df.copy())
        return self.df.copy()

    def find_team_averages(self, team, num_games=8):
        team = team.drop(columns=["team", "season"])
        rolling = team.rolling(num_games).mean()
        return rolling

    def get_essentials(self, df):
        self.essentials = concat_df(df.copy(), self.df.copy())

        for col in self.essentials.columns:
            if (
                (f"_{self.num_games}" not in col)
                & (col != "game_id")
                & (col != "team")
                & (col != "season")
            ):
                self.essentials = self.essentials.drop(columns=[col])
        return self.essentials.copy()
