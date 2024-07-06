from src.utility.constants import CONDITIONALS


# MARK: Query Builder - FInal
def query_builder(
    table_name: str, vars: list[str], conds: list[str], vals: list[str | int | float]
) -> str:
    query: str = f"SELECT * FROM {table_name}"

    if len(vars) == 0: 
        return query + ";"
    else:
        query += " WHERE "

    for i, var in enumerate(iterable=vars):
        for cond in conds:
            if cond in CONDITIONALS:
                query += f"{var} {cond} {vals[i]} AND "

    query = query[:-5] + ";"  # Remove the last "AND" and add a semicolon
    return query


# ! This function is not used currently.
def convert_str_cond(cond: str) -> str:
    if cond == "=":
        return "LIKE"
    if cond == "!=":
        return "NOT LIKE"
    return cond
