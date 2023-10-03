import pandas as pd

from datetime import datetime
from scipy import stats

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.constants import *

from src.relative_data.power_rank import *

# Purpose: RUNNING STRENGTH OF SCHEDULES FOR EACH TEAM


# info: Power Rank over Expectation based on Strength of Schedule (implied)
def sos__roe(pr, gp):
    sos = pd.Series()

    for col in gp.columns:
        sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    exp_pr = pr.mean() * 2 - sos.copy()

    roe = pr.copy() - exp_pr.copy()

    return roe.sort_values(ascending=False).copy()


# info: Adjust Power Rank for Strength of Schedule
# ! This does not have much mathematical backing
def sos__adjust(pr, gp):
    sos = pd.Series()

    for col in gp.columns:
        sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    sos = pr.copy() * (1 + sos - sos.mean())

    return sos.sort_values(ascending=False).copy()


# info: SoS based on Power Rank (implied)
def sos__implied(df, season, game_date, initial_date="", HA=""):
    pr = power_rank__implied(df, season, game_date, initial_date, HA)
    gp = matchup_odds_matrix(df, season, game_date, initial_date)["gp"]
    sos = pd.Series()

    for col in gp.columns:
        sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    return sos.sort_values(ascending=False).copy()


# info: SoS based on Power Rank (implied & matchup weighted)
def sos__implied_matchup(df, season, game_date, initial_date="", HA=""):
    pr = power_rank__implied_matchup(df, season, game_date, initial_date, HA)
    gp = matchup_odds_matrix(df, season, game_date, initial_date)["gp"]
    sos = pd.Series()

    for col in gp.columns:
        sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    return sos.sort_values(ascending=True).copy()
