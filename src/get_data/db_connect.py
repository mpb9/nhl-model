import pymysql


def get_db_connection():
    connection = pymysql.connect(
        host="localhost", user="mpb9", password="9Chester!", database="betting"
    )
    return connection
