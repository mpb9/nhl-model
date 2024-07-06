import pandas as pd
from src.get_data.db_connect import get_conn
    
# ! pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. 
# ! Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
def get_df(query: str) -> pd.DataFrame:
    """_summary_: This function queries the database and returns a DataFrame."""
    return pd.read_sql(sql=query, con=get_conn())
     