import pandas as pd

from datetime import datetime

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.constants import *

# Purpose: RUNNING POWER RANKS FOR EACH TEAM


# info: Ranks weighted by avg odds vs each opponent
def power_rank__implied(df, season, game_date, initial_date="", HA=""):
    if HA == "H":
        pr = matrix_2_power_rank(
            matchup_odds_matrix_HA(
                df, season, game_date, HA="H", initial_date=initial_date
            )["mtrx"],
            ignored_val=0,
        )
    elif HA == "A":
        pr = matrix_2_power_rank(
            matchup_odds_matrix_HA(
                df, season, game_date, HA="A", initial_date=initial_date
            )["mtrx"],
            ignored_val=0,
        )
    else:
        pr = matrix_2_power_rank(
            matchup_odds_matrix(df, season, game_date, initial_date)["mtrx"],
            ignored_val=0,
        )
    return pr.copy()


# info: Ranks weighted by ranked avg odds vs each opponent
def power_rank__implied_matchup(df, season, game_date, initial_date="", HA=""):
    if HA == "":
        mtrx = matchup_odds_matrix(df, season, game_date, initial_date)["mtrx"]
    else:
        mtrx = matchup_odds_matrix_HA(
            df, season, game_date, HA, initial_date=initial_date
        )["mtrx"]

    pr = mtrx.copy().apply(get_number_rank, axis=1)
    pr = matrix_2_power_rank(pr, ignored_val=0, asc=True)
    return pr.copy()


# info: Helper to rank each team given their power rank score(s)
def get_number_rank(pr, asc=False):
    pr = pr.sort_values(ascending=asc)
    for i in range(pr.isnull().value_counts()[False]):
        pr.iloc[i] = i + 1
    return pr.copy()


# info: Helper to convert matrix to power rank
def matrix_2_power_rank(mtrx, ignored_val=0, asc=False):
    return mtrx[mtrx != ignored_val].mean().sort_values(ascending=asc).copy()


# info: Matrix of avg odds vs each opponent
def matchup_odds_matrix(df, season, game_date, initial_date=""):
    teams = get_NHL_teams()

    mtrx = pd.DataFrame(
        [[0] * len(teams) for i in range(len(teams))],
        list(teams.team_name),
        list(teams.team_name),
    )

    count_mtrx = mtrx.copy()

    df = df[df.season == season].copy()
    df = df.drop_duplicates("game_id").copy()

    game_date = datetime.strptime(game_date, "%m/%d/%Y")
    df["game_date"] = pd.to_datetime(df["game_date"])
    df = df[df.game_date < game_date]

    if initial_date != "":
        initial_date = datetime.strptime(initial_date, "%m/%d/%Y")
        df = df[df.game_date >= initial_date]

    for index, row in df.iterrows():
        count_mtrx[row.team][row.opp_team] += 1
        count_mtrx[row.opp_team][row.team] += 1
        prev_matchups = count_mtrx[row.team][row.opp_team].copy()

        # Update HOME team odds
        mtrx.loc[row.opp_team, row.team] = (
            mtrx[row.team][row.opp_team] * (prev_matchups - 1) + row.odds
        ) / prev_matchups

        # Update AWAY team odds
        mtrx.loc[row.team, row.opp_team] = (
            mtrx[row.opp_team][row.team] * (prev_matchups - 1) + row.opp_odds
        ) / prev_matchups

    return {"mtrx": mtrx[mtrx != 0].copy(), "gp": count_mtrx.copy()}


# info: Matrix of avg odds vs each opponent as HOME/AWAY
def matchup_odds_matrix_HA(df, season, game_date, HA="H", initial_date=""):
    teams = get_NHL_teams()

    mtrx = pd.DataFrame(
        [[0] * len(teams) for i in range(len(teams))],
        list(teams.team_name),
        list(teams.team_name),
    )

    count_mtrx = mtrx.copy()

    df = df[df.season == season].copy()
    if HA == "H":
        df = df[df.is_home == 1].copy()
    elif HA == "A":
        df = df[df.is_home == 0].copy()

    game_date = datetime.strptime(game_date, "%m/%d/%Y")
    df["game_date"] = pd.to_datetime(df["game_date"])
    df = df[df.game_date < game_date]

    if initial_date != "":
        initial_date = datetime.strptime(initial_date, "%m/%d/%Y")
        df = df[df.game_date >= initial_date]

    for index, row in df.iterrows():
        count_mtrx[row.team][row.opp_team] += 1
        prev_matchups = count_mtrx[row.team][row.opp_team].copy()

        # Update team odds
        mtrx.loc[row.opp_team, row.team] = (
            mtrx[row.team][row.opp_team] * (prev_matchups - 1) + row.odds
        ) / prev_matchups

    return {"mtrx": mtrx[mtrx != 0].copy(), "gp": count_mtrx.copy()}
