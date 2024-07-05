from flask import Blueprint, render_template
from api_config.utils.paths.web_path_config import WebPage, WebPageHtml
from api_config.utils.paths.api_path_config import Glossary

bp = Blueprint(name="pages", import_name=__name__)


# MARK: Web Page Pages
@bp.route(rule=WebPage.HOME.value)
def home() -> str:
    return render_template(template_name_or_list=WebPageHtml.HOME.value)


@bp.route(rule=WebPage.TOC.value)
def toc() -> str:
    return render_template(template_name_or_list=WebPageHtml.TOC.value)


@bp.route(rule=WebPage.GLOSSARY.value)
def glossary() -> str:
    return render_template(template_name_or_list=WebPageHtml.GLOSSARY.value)


# MARK: API Paths
# @bp.route(rule=Glossary.GET_SEASONS.value)
# def glossary_get_seasons() -> str:
#     return render_template(template_name_or_list="")

# ! not yet implemented
# @bp.route(rule="/team_5on5")
# def team_5on5() -> str:
#     return render_template(template_name_or_list="pages/team_5on5/data.html")


# @bp.route(rule="/team_5on5/odds")
# def team_5on5_odds() -> str:
#     return render_template(template_name_or_list="pages/team_5on5/odds.html")
