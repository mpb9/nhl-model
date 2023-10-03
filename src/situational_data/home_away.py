import pandas as pd

from datetime import datetime

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.constants import *

from src.relative_data.power_rank import *


# Purpose: RUNNING HOME/AWAY ADVANTAGE FOR EACH TEAM


# info: Adjust Power Rank for Home Ice Advantage
def home_ice__adjust(df, season, game_date, initial_date=""):
    base = power_rank__implied(df, season, game_date, initial_date)
    home_ice = home_away_adv__implied(df, season, game_date, "H", initial_date)
    return (base + (home_ice.mean() - home_ice)).sort_values(ascending=False).copy()


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

    return (base + (home_ice.mean() - home_ice)).sort_values(ascending=False).copy()


# info: Home/Away Advantage based on Power Rank (implied)
# adv = HA_Rank - Rank
def home_away_adv__implied(df, season, game_date, HA="H", initial_date=""):
    adv = power_rank__implied(
        df, season, game_date, initial_date, HA
    ) - power_rank__implied(df, season, game_date, initial_date)
    return adv.sort_values(ascending=False).copy()


# info: Home/Away Advantage based on Power Rank (implied & matchup weighted)
# adv = HA_Rank - Rank
def home_away_adv__implied_matchup(df, season, game_date, HA="H", initial_date=""):
    adv = power_rank__implied_matchup(
        df, season, game_date, initial_date, HA
    ) - power_rank__implied_matchup(df, season, game_date, initial_date)
    return adv.sort_values(ascending=True).copy()
