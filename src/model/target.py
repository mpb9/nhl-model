import re
import pandas as pd

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.utility.constants import *

# Purpose: ADD TARGET TO MODEL


def add_model_target(df, target_name, szn, sit):
    df = df.dropna(subset=["next_game_id"]).copy()

    target_data = retrieve_csv("", sit, "target", "")
    target_data = target_data.loc[target_data["season"] == szn][target_name].copy()
    target = target_data[target_name]
    return


def save_target(df, sit, target_name):
    df = rename_col(
        df[["next_game_id", "team", "target"]].copy(),
        "next_game_id",
        "target_game_id",
    )
    df = rename_col(df, "target", target_name)

    target_df = retrieve_csv("", sit, "target", "")
    target_df = pd.merge(target_df, df, on=["target_game_id", "team"])

    export_csv(target_df, "", sit, name="target", subfol="", tidy=False)
    return


def create_custom_target(df, target_cols, operations=[], include_null=False):
    df_target = df.dropna(subset=["next_game_id"]).copy()

    if len(operations) == 0:
        for index, row in df_target.iterrows():
            target_data = df.loc[
                ((df["game_id"] == row["next_game_id"]) & (df["team"] == row["team"]))
            ].iloc[0]
            target = target_data[target_cols[0]]
            df_target.loc[index, "target"] = target
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
            df_target.loc[index, "target"] = target

    IGNORED_COLS.append("target")

    if include_null:
        return include_null_target(df_target, df, "target", len(df.columns))

    return organize(df_target)


def profit_target(df, include_null=False):
    df_target = df.dropna(subset=["next_game_id"]).copy()
    for index, row in df_target.iterrows():
        target_data = df.loc[
            ((df["game_id"] == row["next_game_id"]) & (df["team"] == row["team"]))
        ].iloc[0]
        df_target.loc[index, "profit"] = (
            -1 if target_data["reg_win"] == 0 else (1 / target_data["odds"]) - 1
        )

    IGNORED_COLS.append("profit")

    if include_null:
        return include_null_target(df_target, df, "profit", len(df.columns))

    return organize(df_target)


def include_null_target(df_w_target, df_orig, target_name, target_index):
    df_sans_target = df_orig[pd.isnull(df_orig["next_game_id"])].copy()
    df_sans_target.insert(target_index, target_name, None)
    df_w_target = pd.concat([df_w_target, df_sans_target], ignore_index=True)
    return organize(df_w_target)
