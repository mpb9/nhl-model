import pandas as pd


def orderby_id(df, col_name="game_id"):
    df = df.sort_values(by=col_name, ascending=True)
    df.reset_index(drop=True, inplace=True)
    return df


def orderby_mult(df, col_name_1="game_id", col_name_2="team"):
    df = df.sort_values(by=[col_name_1, col_name_2], ascending=[True, True])
    df.reset_index(drop=True, inplace=True)
    return df


def shift_col(team, col_name, shift=-1):
    next_col = team[col_name].shift(shift)
    return next_col


def add_next_col(df, col_name):
    col = df.groupby("team", group_keys=False).apply(lambda x: shift_col(x, col_name))
    df[f"next_{col_name}"] = col
    return orderby_id(df.copy())


def merge_data(df_1, df_2):
    df_new = pd.concat([df_1.copy(), df_2.copy()], axis=1)
    df_new = df_new.dropna()
    return orderby_id(df_new.copy())


def merge_team_data(df, common_cols, team_x, team_y, on_col):
    df = df.merge(
        df[common_cols + [team_x, team_y, on_col]],
        left_on=[team_x, on_col],
        right_on=[team_y, on_col],
    )
    return orderby_id(df.copy())
