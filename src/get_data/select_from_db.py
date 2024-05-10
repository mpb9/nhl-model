"""_summary_: This file queries database to generate basic dataframes."""

import pandas as pd

from src.get_data.db_connect import get_conn, get_cursor


def get_db(table_name: str) -> pd.DataFrame:
    """_summary_: This function returns a DataFrame from an entire database."""
    conn = get_conn()
    cursor = get_cursor(conn)

    cursor.execute(f"SELECT * FROM {conn.database}.{conn.schema}.{table_name};")

    return pd.DataFrame(
        cursor.fetchall(), columns=[col[0] for col in cursor.description]
    )


def get_db_query(query: str) -> pd.DataFrame:
    """_summary_: This function queries the database and returns a DataFrame."""
    return pd.read_sql(sql=query, con=get_conn())
