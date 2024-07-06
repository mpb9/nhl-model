from flask import Blueprint
from pandas import DataFrame, to_numeric
from gui.controller.utils.format_response import response_builder

from src.get_data.df_service import execute_get_request

# MARK: PATH: /api/glossary
bp = Blueprint(name="glossary", import_name=__name__)
bp.url_prefix = "/api/glossary"


# MARK: GET /seasons
@bp.route(rule="/seasons", methods=["GET"])
def get_seasons() -> str:
    df: DataFrame = execute_get_request(table_name="seasons", vars=[], conds=[], vals=[])
    return response_builder(df=df)


# MARK: GET /teams
@bp.route(rule="/teams", methods=["GET"])
def get_teams() -> str:
    df: DataFrame = execute_get_request(table_name="teams", vars=[], conds=[], vals=[])
    return response_builder(df=df)