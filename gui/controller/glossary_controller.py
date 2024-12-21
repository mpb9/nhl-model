from flask import Blueprint
from pandas import DataFrame
from gui.utils.format_response import response_builder

from src.get_data.df_service import get

# MARK: PATH: /api/glossary
bp = Blueprint(name="glossary", import_name=__name__)
bp.url_prefix = "/api/glossary"


# MARK: GET /seasons
@bp.route(rule="/seasons", methods=["GET"])
def get_seasons() -> str:
    df: DataFrame = get(table_name="seasons", vars=[], conds=[], vals=[])
    df_formatted = response_builder(df=df)
    return df_formatted
    # df_template: str = table_builder(df=df)
    # return render_template_string(source=df_template)


# MARK: GET /teams
@bp.route(rule="/teams", methods=["GET"])
def get_teams() -> str:
    df: DataFrame = get(table_name="teams", vars=[], conds=[], vals=[])
    df_formatted = response_builder(df=df)
    return df_formatted
    # df_template: str = table_builder(df=df)
    # return render_template_string(source=df_template)
