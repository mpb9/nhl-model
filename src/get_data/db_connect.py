"""_summary_: This file contains the connection to the Snowflake database."""

import os
import snowflake.connector
from snowflake.connector.cursor import SnowflakeCursor

# info: Snowflake connection
PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
USER = os.getenv("SNOWFLAKE_USER")
ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")
ORGANIZATION = os.getenv("SNOWFLAKE_ORGANIZATION")
IDENTIFIER = os.getenv("SNOWFLAKE_IDENTIFIER")
ROLE = os.getenv("SNOWFLAKE_ROLE")
REGION = os.getenv("SNOWFLAKE_REGION")
TABLE = os.getenv("SNOWFLAKE_TABLE")


def get_conn():
    """_summary_: This function connects to the Snowflake database."""
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA,
        table=TABLE,
    )
    return conn


def get_cursor(conn: snowflake.connector.connection.SnowflakeConnection):
    """_summary_: This function gets a cursor for the Snowflake connection."""
    return conn.cursor()
