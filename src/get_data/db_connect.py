import os
import snowflake.connector as sc

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

PRIVATE_KEY_FILE = os.getenv("SNOWFLAKE_PRIVATE_KEY_FILE")
PRIVATE_KEY_FILE_PWD = os.getenv("SNOWFLAKE_PRIVATE_KEY_FILE_PWD")

ctx_params = {
    "account": ACCOUNT,
    "user": USER,
    "password": PASSWORD,
    "warehouse": WAREHOUSE,
    "database": DATABASE,
    "schema": SCHEMA,
    "private_key_file": PRIVATE_KEY_FILE,
    "private_key_file_pwd": PRIVATE_KEY_FILE_PWD,
}


# https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#module-snowflake-connector
def get_conn():
    conn = sc.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA,
        table=TABLE,
    )
    print(f"\nget_conn()\n{conn}\n")
    return conn


def get_ctx():
    ctx = sc.connect(**ctx_params)
    print(f"\nget_ctx()\n{ctx}\n")
    return ctx


def get_cursor():
    ctx = sc.connect(**ctx_params)
    cs = ctx.cursor()
    return cs
