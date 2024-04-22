import pandas as pd

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.utility.constants import *

from src.relative_data.power_rank import *


# Purpose: RUNNING HOME/AWAY ADVANTAGE FOR EACH TEAM
# info: Each HOME/AWAY includes all data PRIOR to game_date (might change later to be inclusive)


def home_away(df, pr_type="imp", num_days=500, HA=""):
    pr = pd.DataFrame()

    for season in df["season"].unique():
        df_szn = df[df.season == season].copy()

        for game_date in df_szn["game_date"].unique():
            initial_date = datetime.strptime(game_date, "%Y-%m-%d") - timedelta(
                days=num_days
            )
            initial_date = initial_date.strftime("%Y-%m-%d")

            if pr_type == "adj":
                pr_date = home_ice__adjust(
                    df_szn.copy(), season, game_date, initial_date
                )
            elif pr_type == "adj_matchup":
                pr_date = home_ice__adjust_matchup(
                    df_szn.copy(), season, game_date, initial_date
                )
            elif pr_type == "imp":
                pr_date = home_away_adv__implied(
                    df_szn.copy(), season, game_date, HA, initial_date
                )
            elif pr_type == "imp_matchup":
                pr_date = home_away_adv__implied_matchup(
                    df_szn.copy(), season, game_date, HA, initial_date
                )

            pr = pd.concat([pr, pr_date.to_frame().T], ignore_index=True)

    return pr.copy()


# info: Adjust Power Rank for Home Ice Advantage
def home_ice__adjust(df, season, game_date, initial_date=""):
    base = power_rank__implied(df, season, game_date, initial_date)
    home_ice = home_away_adv__implied(df, season, game_date, "H", initial_date)

    game_date = base[0]
    base = base.iloc[1:]
    home_ice = home_ice.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    return pd.concat(
        [
            date,
            (base + (home_ice.mean() - home_ice)).sort_values(ascending=False).copy(),
        ]
    )


# info: Adjust Power Rank for Home Ice Advantage (matchup sepecific)
def home_ice__adjust_matchup(df, season, game_date, initial_date=""):
    home_mtrx = matchup_odds_matrix_HA(
        df, season, game_date, HA="H", initial_date=initial_date
    )["mtrx"]
    away_mtrx = matchup_odds_matrix_HA(
        df, season, game_date, HA="A", initial_date=initial_date
    )["mtrx"]

    for h in range(len(home_mtrx)):
        for a in range(len(home_mtrx)):
            if away_mtrx.iloc[a, h] is None:
                home_mtrx.iloc[a, h] = None
            else:
                home_mtrx.iloc[a, h] -= away_mtrx.iloc[a, h].copy()

    home_ice = matrix_2_power_rank(home_mtrx.copy())
    base = power_rank__implied(df, season, game_date, initial_date)

    game_date = base[0]
    base = base.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    return pd.concat(
        [
            date,
            (base + (home_ice.mean() - home_ice)).sort_values(ascending=False).copy(),
        ]
    )


# info: Home/Away Advantage based on Power Rank (implied)
# adv = HA_Rank - Rank
def home_away_adv__implied(df, season, game_date, HA="H", initial_date=""):
    home_ice = power_rank__implied(df, season, game_date, initial_date, HA)
    base = power_rank__implied(df, season, game_date, initial_date)

    game_date = base[0]
    base = base.iloc[1:]
    home_ice = home_ice.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    adv = home_ice - base
    return pd.concat([date, adv.sort_values(ascending=False).copy()])


# info: Home/Away Advantage based on Power Rank (implied & matchup weighted)
# adv = HA_Rank - Rank
def home_away_adv__implied_matchup(df, season, game_date, HA="H", initial_date=""):
    home_ice = power_rank__implied_matchup(df, season, game_date, initial_date, HA)
    base = power_rank__implied_matchup(df, season, game_date, initial_date)

    game_date = base[0]
    base = base.iloc[1:]
    home_ice = home_ice.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    adv = home_ice - base
    return pd.concat([date, adv.sort_values(ascending=True).copy()])
