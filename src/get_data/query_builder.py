from src.get_data.db_connect import get_conn
from src.utility.constants import CONDITIONALS


def query_builder(
    table_name: str, vars: list[str], conds: list[str], vals: list[any]
) -> str:
    query = f"SELECT * FROM {table_name} WHERE "

    for i, var in enumerate(vars):
        for cond in CONDITIONALS:
            if conds[i] == cond:
                query += f"{var} {cond} {vals[i]} AND "

    query = query[:-5]
    return query + ";"
