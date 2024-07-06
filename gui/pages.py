from flask import Blueprint, render_template
from gui.utils.path_config import Interface, GuiEndpoint, GuiFilePath

# from api.utils.paths.api_path_config import Glossary

bp = Blueprint(name="pages", import_name=__name__)
bp.url_prefix = Interface.GUI.value


# MARK: Web Page Pages
@bp.route(rule=GuiEndpoint.HOME.value)
def home() -> str:
    return render_template(template_name_or_list=GuiFilePath.HOME.value)


@bp.route(rule=GuiEndpoint.CONTENTS.value)
def contents() -> str:
    return render_template(template_name_or_list=GuiFilePath.CONTENTS.value)


@bp.route(rule=GuiEndpoint.GLOSSARY.value)
def glossary() -> str:
    return render_template(template_name_or_list=GuiFilePath.GLOSSARY.value)


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
