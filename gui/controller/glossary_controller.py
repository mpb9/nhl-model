from flask import Blueprint
from pandas import DataFrame, to_numeric

from src.get_data.query_builder import query_builder
from gui.view.response_builder import response_builder
from src.get_data.select_from_db import get_db_query

# MARK: PATH: /api/glossary
bp = Blueprint(name="glossary", import_name=__name__)
bp.url_prefix = "/api/glossary"


# MARK: GET /seasons
@bp.route(rule="/seasons", methods=["GET"])
def get_seasons() -> str:
    query: str = query_builder(table_name="seasons", vars=[], conds=[], vals=[])
    df: DataFrame = get_db_query(query=query)
    return response_builder(df=df)


# MARK: GET /teams
@bp.route(rule="/teams", methods=["GET"])
def get_teams() -> str:
    query: str = query_builder(table_name="teams", vars=[], conds=[], vals=[])
    df: DataFrame = get_db_query(query=query)
    return response_builder(df=df)