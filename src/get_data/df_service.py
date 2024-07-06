from src.utility.constants import CONDITIONALS
from src.get_data.df_repository import get_df

# MARK: Builds SnowSQL query
def execute_get_request(table_name: str, vars: list[str], conds: list[str], vals: list[str | int | float]
) -> str:
    query = f"SELECT * FROM {table_name}"
    if len(vars) == 0:
        return get_df(query=query + ";")
    query += " WHERE "
    
    for i, var in enumerate(iterable=vars):
        for cond in conds:
            if cond in CONDITIONALS:
                query += f"{var} {cond} {vals[i]} AND "

    return get_df(query[:-5] + ";")

# ! This function is not used currently.
def convert_str_cond(cond: str) -> str:
    if cond == "=":
        return "LIKE"
    if cond == "!=":
        return "NOT LIKE"
    return cond
