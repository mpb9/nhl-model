import pandas as pd

from sklearn.model_selection import TimeSeriesSplit
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from .constants import MODEL_CONST
from .init_DFs.per_game import PerGameInit


class PerGameModel:
    def __init__(self):
        self.ignored_cols = MODEL_CONST["IGNORED_COLS"]
        self.per_game_init = PerGameInit()
        self.reorder_col = self.per_game_init.reorder_col

    def add_target(
        self, df, target_name, target_cols, operations=[], include_null_targets=False
    ):
        df_target = df.dropna(subset=["next_game_id"]).copy()

        if len(operations) == 0:
            for index, row in df_target.iterrows():
                target_data = df.loc[
                    (
                        (df["game_id"] == row["next_game_id"])
                        & (df["team"] == row["team"])
                    )
                ].iloc[0]
                target = target_data[target_cols[0]]
                df_target.loc[index, target_name] = target
        else:
            for index, row in df_target.iterrows():
                target_data = df.loc[
                    (
                        (df["game_id"] == row["next_game_id"])
                        & (df["team"] == row["team"])
                    )
                ].iloc[0]
                target = target_data[target_cols[0]]
                for i in range(len(operations)):
                    if operations[i] == "+":
                        target += target_data[target_cols[i + 1]]
                    elif operations[i] == "-":
                        target -= target_data[target_cols[i + 1]]
                    elif operations[i] == "*":
                        target *= target_data[target_cols[i + 1]]
                    elif operations[i] == "/":
                        target /= target_data[target_cols[i + 1]]
                df_target.loc[index, target_name] = target

        self.ignored_cols.append(target_name)

        if include_null_targets:
            return self.add_data_without_valid_target(
                df_target, df, target_name, len(df.columns)
            )

        return self.sort(df_target, "game_id")

    def add_placebo(
        self, df, placebo_name, placebo_cols, operations=[], include_null_targets=False
    ):
        return self.add_target(
            df, placebo_name, placebo_cols, operations, include_null_targets
        )

    def add_data_without_valid_target(
        self, df_w_target, df_orig, target_name, target_index
    ):
        df_sans_target = df_orig[pd.isnull(df_orig["next_game_id"])].copy()
        df_sans_target.insert(target_index, target_name, None)
        df_w_target = pd.concat([df_w_target, df_sans_target], ignore_index=True)
        return self.sort(df_w_target, "game_id")

    def season_backtest(self, data, model, predictors, target, start=2, step=1):
        all_predictions = []
        seasons = sorted(data["season"].unique())

        for i in range(start, len(seasons), step):
            season = seasons[i]

            train = data[data["season"] < season]
            test = data[data["season"] == season]

            model.fit(train[predictors], train[target])

            preds = model.predict(test[predictors])
            preds = pd.Series(preds, index=test.index)

            combined = pd.concat([test[target], preds], axis=1)
            combined.columns = ["actual", "predicted"]

            all_predictions.append(combined)
        return pd.concat(all_predictions)

    def find_team_averages(self, team, num_games=8):
        team = team.drop(columns=["team", "season"])
        rolling = team.rolling(num_games).mean()
        return rolling

    def shift_col(self, team, col_name):
        next_col = team[col_name].shift(-1)
        return next_col

    def add_col(self, df, col_name):
        return df.groupby("team", group_keys=False).apply(
            lambda x: self.shift_col(x, col_name)
        )

    def sort(self, df, col_name="game_id"):
        df = df.sort_values(by=col_name, ascending=True)
        df.reset_index(drop=True, inplace=True)
        return df
