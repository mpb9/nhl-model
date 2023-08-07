import os
import pandas as pd
from src.constants import *
from src.utility import *
from src.rolling_data import RollingData
from src.per_game_model import PerGameModel
from src.init_DFs.per_game import PerGameInit
from src.init_DFs.next_game import NextGameInit

pgModel = PerGameModel()
initPG = PerGameInit()
initNextGame = NextGameInit()


def quick_init__per_game(
    season_arr,
    situation_arr,
    auto_export=True,
):
    results = []
    for season in season_arr:
        for situation in situation_arr:
            games = pd.read_csv(CSV_DB_PATH + f"{season}/games_{season}.csv")
            team_SIT = pd.read_csv(
                CSV_DB_PATH + f"{season}/team_x_game_{situation}_{season}.csv"
            )
            odds = pd.read_csv(CSV_DB_PATH + f"{season}/odds_x_game_{season}.csv")

            pg = pd.merge(pd.merge(team_SIT, games), odds)

            pg = initPG.init_per_game(pg)
            pg.to_csv(
                CSV_TEMP_PATH + f"PER_GAME_{situation}_{season}.csv",
                header=True,
                index=False,
            )

            pg_copy = pg.copy()
            pg_teams = initPG.init_by_team(pg, pg_copy)
            pg_teams.to_csv(
                CSV_TEMP_PATH + f"PER_GAME_BY_TEAM_{situation}_{season}.csv",
                header=True,
                index=False,
            )

            if auto_export:
                pg.to_csv(
                    CSV_DB_PATH + f"{season}/PER_GAME_{situation}_{season}.csv",
                    header=True,
                    index=False,
                )
                os.remove(CSV_TEMP_PATH + f"PER_GAME_{situation}_{season}.csv")

                pg_teams.to_csv(
                    CSV_DB_PATH + f"{season}/PER_GAME_BY_TEAM_{situation}_{season}.csv",
                    header=True,
                    index=False,
                )
                os.remove(CSV_TEMP_PATH + f"PER_GAME_BY_TEAM_{situation}_{season}.csv")
    return results


def quick_init__rolling(
    season_arr,
    situation_arr,
    num_games_arr,
    groupby_cols=["team", "season"],
    include_null_next=True,
    include_null_targets=True,
    null_target_value=2,
    target="next_reg_win",
    target_cols=["reg_win"],
    target_operations=[],
    auto_export=True,
):
    results = []
    for num_games in num_games_arr:
        for season in season_arr:
            for situation in situation_arr:
                df = pd.read_csv(
                    CSV_DB_PATH + f"{season}/PER_GAME_BY_TEAM_{situation}_{season}.csv"
                )

                if include_null_targets:
                    df = pgModel.add_target(
                        df, target, target_cols, target_operations, include_null_targets
                    )
                    df[target].fillna(null_target_value, inplace=True)
                else:
                    df = pgModel.add_target(df, target, target_cols, target_operations)

                selected_cols = df.columns[~df.columns.isin(IGNORED_COLS)]

                rolling = RollingData(
                    df.copy(), selected_cols, num_games, include_null_next, groupby_cols
                )

                rolling.essentials.to_csv(
                    CSV_TEMP_PATH + f"ROLLING_{num_games}_{situation}_{season}.csv",
                    header=True,
                    index=False,
                )

                results.append(rolling)

                if auto_export:
                    rolling.essentials.to_csv(
                        CSV_DB_PATH
                        + f"{season}/ROLLING_{num_games}_{situation}_{season}.csv",
                        header=True,
                        index=False,
                    )
                    os.remove(
                        CSV_TEMP_PATH + f"ROLLING_{num_games}_{situation}_{season}.csv"
                    )
    return results


def quick_init__all(
    season_arr,
    situation_arr,
    num_games_arr,
    groupby_cols=["team", "season"],
    include_null_next=True,
    include_null_targets=True,
    null_target_value=2,
    target="next_reg_win",
    target_cols=["reg_win"],
    target_operations=[],
    auto_export=True,
):
    results = []
    results.append(quick_init__per_game(season_arr, situation_arr, auto_export))
    results.append(
        quick_init__rolling(
            season_arr,
            situation_arr,
            num_games_arr,
            groupby_cols,
            include_null_next,
            include_null_targets,
            null_target_value,
            target,
            target_cols,
            target_operations,
            auto_export,
        )
    )
    return results
