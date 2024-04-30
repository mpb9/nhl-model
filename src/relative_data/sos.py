import pandas as pd

from src.utility.storage import *
from src.utility.structure import *
from src.utility.personal import *
from src.utility.constants import *

from src.relative_data.power_rank import *

# Purpose: RUNNING STRENGTH OF SCHEDULES FOR EACH TEAM
# info: Each SOS includes all data PRIOR to game_date (might change later to be inclusive)


def sos(df, pr_type="imp", num_days=500, HA=""):
    pr = pd.DataFrame()

    for season in df["season"].unique():
        df_szn = df[df.season == season].copy()

        for game_date in df_szn["game_date"].unique():
            initial_date = datetime.strptime(game_date, "%Y-%m-%d") - timedelta(
                days=num_days
            )
            initial_date = initial_date.strftime("%Y-%m-%d")

            if pr_type == "imp":
                pr_date = sos__implied(df_szn.copy(), season, game_date, initial_date)
            elif pr_type == "roe":
                pr_imp = power_rank__implied(
                    df_szn.copy(), season, game_date, initial_date
                )
                odds = matchup_odds_matrix(
                    df_szn.copy(), season, game_date, initial_date
                )
                pr_date = sos__roe(
                    pr_imp,
                    odds["gp"].copy(),
                )
            elif pr_type == "adj":
                pr_date = sos__adjust(
                    power_rank__implied(df_szn.copy(), season, game_date, initial_date),
                    matchup_odds_matrix(df_szn.copy(), season, game_date, initial_date)[
                        "gp"
                    ].copy(),
                )
            elif pr_type == "imp_matchup":
                pr_date = sos__implied_matchup(
                    df_szn.copy(), season, game_date, initial_date
                )

            pr = pd.concat([pr, pr_date.to_frame().T], ignore_index=True)

    return pr.copy()


# info: Power Rank over Expectation based on Strength of Schedule (implied)
def sos__roe(pr, gp):
    sos = pd.Series()

    game_date = pr[0]
    pr = pr.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    for col in gp.columns:
        if gp[col].sum() == 0:
            sos[col] = None
        else:
            sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    exp_pr = pr.mean() * 2 - sos.copy()

    roe = pr.copy() - exp_pr.copy()

    return pd.concat([date, roe.sort_values(ascending=False).copy()])


# info: Adjust Power Rank for Strength of Schedule
# ! This does not have much mathematical backing
def sos__adjust(pr, gp):
    sos = pd.Series()

    game_date = pr[0]
    pr = pr.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    for col in gp.columns:
        if gp[col].sum() == 0:
            sos[col] = None
        else:
            sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    sos = pr.copy() * (1 + sos - sos.mean())

    return pd.concat([date, sos.sort_values(ascending=False).copy()])


# info: SoS based on Power Rank (implied)
def sos__implied(df, season, game_date, initial_date="", HA=""):
    pr = power_rank__implied(df, season, game_date, initial_date, HA)
    gp = matchup_odds_matrix(df, season, game_date, initial_date)["gp"]
    sos = pd.Series()

    game_date = pr[0]
    pr = pr.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    for col in gp.columns:
        if gp[col].sum() == 0:
            sos[col] = None
        else:
            sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    return pd.concat([date, sos.sort_values(ascending=False).copy()])


# info: SoS based on Power Rank (implied & matchup weighted)
def sos__implied_matchup(df, season, game_date, initial_date="", HA=""):
    pr = power_rank__implied_matchup(df, season, game_date, initial_date, HA)
    gp = matchup_odds_matrix(df, season, game_date, initial_date)["gp"]
    sos = pd.Series()

    game_date = pr[0]
    pr = pr.iloc[1:]
    date = pd.Series()
    date["game_date"] = game_date

    for col in gp.columns:
        if gp[col].sum() == 0:
            sos[col] = None
        else:
            sos[col] = (pr.copy() * gp[col]).sum() / gp[col].sum()

    return pd.concat([date, sos.sort_values(ascending=True).copy()])
