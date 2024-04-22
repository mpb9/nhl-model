from ..utility import *


class NextGameInit:
    def add_next_game_data(self, df):
        df_next = df.dropna(subset=["next_game_id"]).copy()
        for index, row in df_next.iterrows():
            next_game_data = df.loc[
                ((df["game_id"] == row["next_game_id"]) & (df["team"] == row["team"]))
            ].iloc[0]
            df_next.loc[index, "next_win"] = next_game_data["win"]
            df_next.loc[index, "next_reg_win"] = next_game_data["reg_win"]
            df_next.loc[index, "next_overtime"] = next_game_data["overtime"]
            df_next.loc[index, "next_score"] = next_game_data["score"]
            df_next.loc[index, "next_opp_score"] = next_game_data["opp_score"]
            df_next.loc[index, "next_xGoals"] = next_game_data["xGoals"]
            df_next.loc[index, "next_opp_xGoals"] = next_game_data["opp_xGoals"]
            df_next.loc[index, "next_xGoalsPercentage"] = next_game_data[
                "xGoalsPercentage"
            ]
        df_next["next_win"] = df_next["next_win"].astype(int)
        df_next["next_reg_win"] = df_next["next_reg_win"].astype(int)
        df_next["next_overtime"] = df_next["next_overtime"].astype(int)
        df_next["next_score"] = df_next["next_score"].astype(int)
        df_next["next_opp_score"] = df_next["next_opp_score"].astype(int)
        return orderby_id(df_next)

    remove_cols = [
        "game_id",
        "team",
        "opp_team",
        "season",
        "next_game_id",
        "game_date",
        "game_time",
        "situation",
        "is_home",
        "next_win",
        "next_reg_win",
        "next_overtime",
        "next_score",
        "next_opp_score",
        "next_xGoals",
        "next_opp_xGoals",
        "next_xGoalsPercentage",
    ]
