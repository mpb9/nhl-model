from flask import Blueprint
from pandas import DataFrame, to_numeric

from src.get_data.df_service import get
from gui.utils.format_response import response_builder

# MARK: Blueprint: /5on5/team
bp = Blueprint(name="by_team", import_name=__name__)
bp.url_prefix = "/5on5/team"


# MARK: GET /<team>
@bp.route(rule="/<team>", methods=["GET"])
def get_5on5_by_team(team: str) -> dict:
    df: DataFrame = get(
        table_name="team_5on5", vars=["TEAM"], conds=["LIKE"], vals=[team]
    )
    resp: dict = response_builder(df=df)
    return resp


# MARK: GET /season/<season>
@bp.route(rule="/season/<season>", methods=["GET"])
def get_5on5_by_season(season: str) -> dict:
    season_float: float = to_numeric(season)
    season_int: int = int(season_float)

    df: DataFrame = get(
        table_name="team_5on5", vars=["SEASON"], conds=["="], vals=[season_int]
    )
    resp: dict = response_builder(df=df)
    return resp


# MARK: GET /<team>/season/<season>
@bp.route(rule="/<team>/season/<season>", methods=["GET"])
def get_5on5_by_team_and_season(team: str, season: str) -> dict:
    season_int: int = int(to_numeric(season))

    df: DataFrame = get(
        table_name="team_5on5",
        vars=["TEAM", "SEASON"],
        conds=["LIKE", "="],
        vals=[team, season_int],
    )
    resp: dict = response_builder(df=df)
    return resp
