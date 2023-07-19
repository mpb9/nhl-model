import pymysql
from .db_connect import get_db_connection


class UtilityData:
    def __init__(self):
        self.connect = get_db_connection()
        self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)

    def all_games(self):
        self.cursor.execute("SELECT * FROM games")
        rows = self.cursor.fetchall()
        return rows

    def all_teams(self):
        self.cursor.execute("SELECT * FROM teams")
        rows = self.cursor.fetchall()
        return rows

    def all_seasons(self):
        self.cursor.execute("SELECT * FROM seasons")
        rows = self.cursor.fetchall()
        return rows

    def mp_game_id_convert(self, mp_game_id):
        self.cursor.execute(
            "SELECT game_id FROM mp_game_id WHERE mp_game_id = %s", (mp_game_id)
        )
        rows = self.cursor.fetchall()
        return rows[0]["game_id"]

    def all_games_playoff(self):
        self.cursor.execute("SELECT * FROM games_playoff")
        rows = self.cursor.fetchall()
        return rows
