import os

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
