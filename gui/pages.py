from flask import Blueprint, redirect, render_template
from pandas import DataFrame
from gui.utils.format_response import table_builder
from gui.utils.path_config import paths
from src.get_data.df_service import get

bp = Blueprint(name="pages", import_name=__name__)
bp.url_prefix = "/"


# MARK: GUI Pages
@bp.route(rule=paths["GUI"]["home"].url())
def home() -> str:
    return render_template(template_name_or_list=paths["GUI"]["home"].file_path())


@bp.route(rule=paths["GUI"]["contents"].url())
def contents() -> str:
    return render_template(template_name_or_list=paths["GUI"]["contents"].file_path())


@bp.route(rule=paths["GUI"]["glossary"].url())
def glossary() -> str:
    szn_df: DataFrame = get(table_name="seasons", vars=[], conds=[], vals=[])
    seasons: str = table_builder(df=szn_df)

    tm_df: DataFrame = get(table_name="teams", vars=[], conds=[], vals=[])
    teams: str = table_builder(df=tm_df)

    return render_template(
        template_name_or_list=paths["GUI"]["glossary"].file_path(),
        seasons=seasons,
        teams=teams,
    )


# MARK: API Paths
# @bp.route(rule=ApiEndpoint.GLOSSARY.GET_SEASONS.value)
# def glossary_get_seasons() -> str:
#     return render_template(template_name_or_list="")


# ! not yet implemented
# @bp.route(rule='/team_5on5')
# def team_5on5() -> str:
#     return render_template(template_name_or_list='pages/team_5on5/data.html')


# @bp.route(rule='/team_5on5/odds')
# def team_5on5_odds() -> str:
#     return render_template(template_name_or_list='pages/team_5on5/odds.html')


# MARK: Error Handlers


# MARK: Reroute Handlers
@bp.route(rule=paths["UTIL"]["root"].url())
def no_endpoint() -> str:

    paths["UTIL"]["root"].handle_redirect(message="invalid endpoint")

    return redirect(location=paths["GUI"]["home"].url())
