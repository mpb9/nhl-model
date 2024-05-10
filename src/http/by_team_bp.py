from flask import Blueprint
from pandas import DataFrame, to_numeric

from src.get_data.query_builder import query_builder
from src.http.response_builder import response_builder
from src.get_data.select_from_db import get_db_query


# MARK: Blueprint: /5on5/team
bp = Blueprint(name="by_team", import_name=__name__)
bp.url_prefix = "/5on5/team"


# MARK: GET /<team>
@bp.route(rule="/<team>", methods=["GET"])
def get_5on5_by_team(team: str) -> dict:
    query: str = query_builder(
        table_name="team_5on5", vars=["TEAM"], conds=["LIKE"], vals=[team]
    )
    df: DataFrame = get_db_query(query=query)

    resp: dict = response_builder(df=df, query=query)
    return resp


# MARK: GET /season/<season>
@bp.route(rule="/season/<season>", methods=["GET"])
def get_5on5_by_season(season: str) -> dict:
    season_float: float = to_numeric(season)
    season_int: int = int(season_float)

    query: str = query_builder(
        table_name="team_5on5", vars=["SEASON"], conds=["="], vals=[season_int]
    )
    df: DataFrame = get_db_query(query=query)

    resp: dict = response_builder(df=df, query=query)
    return resp


# MARK: GET /<team>/season/<season>
@bp.route(rule="/<team>/season/<season>", methods=["GET"])
def get_5on5_by_team_and_season(team: str, season: str) -> dict:
    season_int: int = int(to_numeric(season))

    query: str = query_builder(
        table_name="team_5on5",
        vars=["TEAM", "SEASON"],
        conds=["LIKE", "="],
        vals=[team, season_int],
    )
    df: DataFrame = get_db_query(query=query)

    resp: dict = response_builder(df=df, query=query)
    return resp
