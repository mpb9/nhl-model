"""_summary_: This file queries database to generate basic dataframes."""

import pandas as pd

from src.get_data.db_connect import get_conn, get_cursor


def get_db(table_name: str) -> pd.DataFrame:
    conn = get_conn()
    cursor = get_cursor(conn)
    team = "TOR"
    cursor.execute(
        f"SELECT * FROM {conn.database}.{conn.schema}.{table_name} WHERE SEASON = 2022;"
    )
    return pd.DataFrame(
        cursor.fetchall(), columns=[col[0] for col in cursor.description]
    )


def get_db_query(query: str) -> pd.DataFrame:
    return pd.read_sql(query, con=get_conn())
