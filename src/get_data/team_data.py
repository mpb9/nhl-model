import pymysql
from .db_connect import get_db_connection


class TeamData:
    def __init__(self):
        self.connect = get_db_connection()
        self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)

    def all_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()
        return rows

    # info: conditions format:
    # [{'header': string, 'equals': bool, 'value': xxx}...]
    def conditional_data(self, table_name, conditions):
        if conditions[0]["equals"]:
            self.cursor.execute(
                f"SELECT * FROM {table_name} WHERE {conditions[0]['header']} = %s",
                (conditions[0]["value"]),
            )
        else:
            self.cursor.execute(
                f"SELECT * FROM {table_name} WHERE {conditions[0]['header']} != %s",
                (conditions[0]["value"]),
            )
        rows = self.cursor.fetchall()

        for condition in conditions[1:]:
            if condition["equals"]:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} WHERE {condition['header']} = %s",
                    (condition["value"]),
                )
            else:
                self.cursor.execute(
                    f"SELECT * FROM {table_name} WHERE {condition['header']} != %s",
                    (condition["value"]),
                )
            temp_rows = self.cursor.fetchall()
            rows = [row for row in rows if row in temp_rows]
        return rows
