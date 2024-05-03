import numpy as np
import pandas as pd

from src.utility.personal import *


class PerGameInit:
    def init_per_game(self, df):
        df = self.next_game_ids_HA(df)
        df = self.reorder_col(df, "away_team", 2)
        df = self.reorder_col(df, "game_time", 5)
        df = self.reorder_col(df, "next_game_id_home", 3)
        df = self.reorder_col(df, "next_game_id_away", 4)
        df = self.reorder_col(df, "season", 1)
        return df

    def init_by_team(self, df_1, df_2):
        df_1 = self.by_team_away(df_1)
        df_2 = self.by_team_home(df_2)
        df = pd.concat([df_1, df_2], axis=0)
        df = self.rename_col(df, "result", "reg_win")
        df = self.rename_col(df, "ot_result", "overtime")
        df["win"] = np.where(df["score"] > df["opp_score"], 1, 0)
        df = df.drop(
            columns=[
                "opp_result",
                "opp_next_game_id",
                "opp_corsiPercentage",
                "opp_fenwickPercentage",
                "opp_xGoalsPercentage",
            ]
        )
        df["win"] = df["win"].astype(int)
        df = add_game_number(df)
        df = add_rest(df)
        return tidy_up(df)

    def next_game_ids_HA(self, df):
        df = self.orderby_id(df)
        for index, row in df.iterrows():
            next_game_id_home = "NA"
            for i in range(index + 1, len(df)):
                if df.loc[i, "season"] != row["season"]:
                    next_game_id_home = "NA"
                    break
                if (
                    df.loc[i, "home_team"] == row["home_team"]
                    or df.loc[i, "away_team"] == row["home_team"]
                ):
                    next_game_id_home = df.loc[i, "game_id"]
                    break
            df.loc[index, "next_game_id_home"] = next_game_id_home
        for index, row in df.iterrows():
            next_game_id_away = "NA"
            for i in range(index + 1, len(df)):
                if df.loc[i, "season"] != row["season"]:
                    next_game_id_away = "NA"
                    break
                if (
                    df.loc[i, "home_team"] == row["away_team"]
                    or df.loc[i, "away_team"] == row["away_team"]
                ):
                    next_game_id_away = df.loc[i, "game_id"]
                    break
            df.loc[index, "next_game_id_away"] = next_game_id_away
        return df

    def prev_game_ids_HA(self, df):
        df = self.orderby_id(df)
        for index, row in df.iterrows():
            prev_game_id_home = "NA"
            for i in range(index - 1, -1, -1):
                if df.loc[i, "season"] != row["season"]:
                    prev_game_id_home = "NA"
                    break
                if (
                    df.loc[i, "home_team"] == row["home_team"]
                    or df.loc[i, "away_team"] == row["home_team"]
                ):
                    prev_game_id_home = df.loc[i, "game_id"]
                    break
            df.loc[index, "prev_game_id_home"] = prev_game_id_home
        for index, row in df.iterrows():
            prev_game_id_away = "NA"
            for i in range(index - 1, -1, -1):
                if df.loc[i, "season"] != row["season"]:
                    prev_game_id_away = "NA"
                    break
                if (
                    df.loc[i, "home_team"] == row["away_team"]
                    or df.loc[i, "away_team"] == row["away_team"]
                ):
                    prev_game_id_away = df.loc[i, "game_id"]
                    break
            df.loc[index, "prev_game_id_away"] = prev_game_id_away
        return df

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
        away_df = self.orderby_id(away_df)
        return away_df

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
        home_df = self.orderby_id(home_df)
        return home_df

    def rename_col(self, df, col_name, new_col_name):
        df.rename(columns={col_name: new_col_name}, inplace=True)
        return df

    def orderby_id(self, df, col_name="game_id"):
        df = df.sort_values(by=col_name, ascending=True)
        df.reset_index(drop=True, inplace=True)
        return df

    def reorder_col(self, df, col_name, new_index):
        column_to_move = df[col_name]
        df = df.drop(columns=col_name)
        df.insert(new_index, col_name, column_to_move)
        return df

    def reorder_by_team_columns(self, df):
        cols_2_move = [
            ["iceTime", 1],
            ["is_home", 1],
            ["rest", 1],
            ["game_time", 1],
            ["game_date", 1],
            ["situation", 1],
            ["ot_odds", 1],
            ["opp_odds", 1],
            ["odds", 1],
            ["overtime", 1],
            ["reg_win", 1],
            ["win", 1],
            ["opp_score", 1],
            ["score", 1],
            ["next_game_id", 1],
            ["game_number", 1],
            ["season", 1],
            ["opp_team", 1],
            ["team", 1],
        ]
        for col_movin in cols_2_move:
            column_to_move = df[col_movin[0]]
            df = df.drop(columns=col_movin[0])
            df.insert(col_movin[1], col_movin[0], column_to_move)
        return df
