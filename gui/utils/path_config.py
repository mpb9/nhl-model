from gui.utils.path import Path, GuiPath

paths = {
    # MARK: GUI Paths
    "GUI": {
        "home": GuiPath(file_name="home"),
        "contents": GuiPath(endpoint="contents", file_name="contents"),
        "glossary": GuiPath(endpoint="glossary", file_name="glossary"),
    },
    # MARK: API Paths
    "API": {
        "data": Path(interface="api", endpoint="data"),
        "models": Path(interface="api", endpoint="models"),
        "glossary": Path(interface="api", endpoint="glossary"),
        "utils": Path(interface="api", endpoint="utils"),
    },
    # MARK: UTIL Paths
    "UTIL": {"root": Path()},
}
