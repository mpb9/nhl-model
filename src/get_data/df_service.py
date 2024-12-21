import pandas as pd
from src.utility.constants import CONDITIONALS
from src.get_data.df_repository import get_df


# MARK: Builds SnowSQL query
def get(
    table_name: str, vars: list[str], conds: list[str], vals: list[str | int | float]
) -> pd.DataFrame:
    query = f"SELECT * FROM DUMPNCHASE.PUBLIC.{table_name}"
    if len(vars) == 0:
        return get_df(f"{query};")
    query += " WHERE "

    for i, var in enumerate(iterable=vars):
        for cond in conds:
            if cond in CONDITIONALS:
                query += f"{var} {cond} {vals[i]} AND "

    query = query[:-5] + ";"
    return get_df(sql=query)
