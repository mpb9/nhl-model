import os
from pandas.io.formats.style import Styler
from pandas import DataFrame

API_ENVIRONMENT: str | None = os.getenv(key="ENVIRONMENT")

TABLE_STYLES = [
    dict(
        **{
            "selector": "",
            "props": [
                ("border-collapse", "collapse"),
                ("border-spacing", "0px"),
                ("font-family", "Ubuntu, sans-serif"),
            ],
        }
    ),
    dict(
        selector="th.col_heading",
        props=[
            ("color", "#e3a33b"),
            ("background-color", "#3c3b38 !important"),
            ("padding", "0.4em 0.5em 0.4em 0.5em"),
            ("text-align", "center"),
            ("border", "1px solid #1f1f1f"),
        ],
    ),
    dict(
        selector="tr",
        props=[("background-color", "#EDEDED")],
    ),
    dict(
        selector="tr:hover",
        props=[
            ("background-color", "#d8d8d8"),
        ],
    ),
    dict(
        selector="tr:hover>td.col0",
        props=[("background-color", "#a8a8a8"), ("font-style", "italic")],
    ),
    dict(
        selector="td",
        props=[
            ("color", "#224e92"),
            ("text-align", "center"),
            ("padding", "0.25em 0.25em 0.25em 0.25em"),
            ("border", "1px solid #414445"),
        ],
    ),
    dict(
        selector="td.col0",
        props=[("background-color", "#c8c8c8"), ("font-weight", "500")],
    ),
]


# MARK: Response Builder
def response_builder(df: DataFrame | None = None) -> str:
    data = df.to_json(orient="records") if df is not None else "Data not found."
    return data


# MARK: HTML Response Builder
def table_builder(df: DataFrame | None = None) -> str:
    s = Styler(data=df, uuid_len=0, cell_ids=False)
    s.set_table_styles(
        table_styles=TABLE_STYLES,
        overwrite=False,
    )
    s.hide(axis="index")
    s.set_sticky(axis="columns")
    return s.to_html()
