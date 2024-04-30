import pandas as pd

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.utility.constants import *

# Purpose: TARGETS FOR MODELING


def add_custom_target(
    df, target_name, target_cols, operations=[], include_null_targets=False
):
    df_target = df.dropna(subset=["next_game_id"]).copy()

    if len(operations) == 0:
        for index, row in df_target.iterrows():
            target_data = df.loc[
                ((df["game_id"] == row["next_game_id"]) & (df["team"] == row["team"]))
            ].iloc[0]
            target = target_data[target_cols[0]]
            df_target.loc[index, target_name] = target
    else:
        for index, row in df_target.iterrows():
            target_data = df.loc[
                ((df["game_id"] == row["next_game_id"]) & (df["team"] == row["team"]))
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

    IGNORED_COLS.append(target_name)

    if include_null_targets:
        return add_data_without_valid_target(
            df_target, df, target_name, len(df.columns)
        )

    return orderby_id(df_target)


def add_profit_target(df, include_null_targets=False):
    df_target = df.dropna(subset=["next_game_id"]).copy()
    for index, row in df_target.iterrows():
        target_data = df.loc[
            ((df["game_id"] == row["next_game_id"]) & (df["team"] == row["team"]))
        ].iloc[0]
        win = target_data["reg_win"]
        odds = target_data["odds"]
        profit = -1.0
        if win == 1:
            profit = profit + (1 / odds)
        df_target.loc[index, "next_profit"] = profit

    IGNORED_COLS.append("next_profit")

    if include_null_targets:
        return add_data_without_valid_target(
            df_target, df, "next_profit", len(df.columns)
        )

    return orderby_id(df_target)


def add_data_without_valid_target(df_w_target, df_orig, target_name, target_index):
    df_sans_target = df_orig[pd.isnull(df_orig["next_game_id"])].copy()
    df_sans_target.insert(target_index, target_name, None)
    df_w_target = pd.concat([df_w_target, df_sans_target], ignore_index=True)
    return orderby_id(df_w_target)
