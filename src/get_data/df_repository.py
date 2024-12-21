import pandas as pd
import snowflake.connector as sc
from src.get_data.db_config import ctx_params


def get_df(query: str) -> pd.DataFrame:
    """_summary_: This function queries the database and returns a DataFrame."""
    res = None

    ctx = sc.connect(**ctx_params)
    cur = ctx.cursor()
    try:
        cur.execute(query)
        res = cur.fetch_pandas_all()
    finally:
        cur.close()
        ctx.close()

    return res
