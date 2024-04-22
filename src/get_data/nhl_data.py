import pymysql
from .db_connect import get_db_connection


class NHLData:
    def __init__(self):
        self.connect = get_db_connection()
        self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)

    def all_data(self, table_name, order_by="game_id"):
        self.cursor.execute(f"SELECT * FROM {table_name} ORDER BY {order_by} ASC")
        rows = self.cursor.fetchall()
        return rows

    # info: conditions format:
    # [{'header': string, 'conditional': CONDITIONALS[i], 'value': any}...]
    def conditional_data(self, table_name, conditions, order_by="game_id"):
        query = f"SELECT * FROM {table_name} WHERE "
        for var in conditions:
            query += f"{var['header']} {var['conditional']} %s AND "
        query = query[:-5]
        query += f" ORDER BY {order_by} ASC"
        self.cursor.execute(
            query, tuple([condition["value"] for condition in conditions])
        )
        rows = self.cursor.fetchall()
        return rows

    def ref_table_conditional_data(
        self, table_name, ref_table_name, ref_header, conditions, order_by="game_id"
    ):
        query = f"SELECT * FROM {table_name} WHERE {ref_header} IN ("
        query += f"SELECT {ref_header} FROM {ref_table_name} WHERE "
        for var in conditions:
            query += f"{var['header']} {var['conditional']} %s AND "
        query = query[:-5]
        query += f") ORDER BY {order_by} ASC"
        self.cursor.execute(
            query, tuple([condition["value"] for condition in conditions])
        )
        rows = self.cursor.fetchall()
        return rows

    # info: methods to get previous game_id(s)
    def all_prev_game_ids(self, order_by="game_id"):
        self.cursor.execute(f"SELECT * FROM games ORDER BY {order_by} ASC")
        rows = self.cursor.fetchall()
        prev_game_ids = []
        for row in rows:
            prev_ids = self.prev_game_ids(row["game_id"])
            prev_game_ids.append(
                {
                    "game_id": row["game_id"],
                    "prev_game_id_home": prev_ids["home"],
                    "prev_game_id_away": prev_ids["away"],
                }
            )
        return prev_game_ids

    def conditional_prev_game_ids(self, conditions, order_by="game_id"):
        query = f"SELECT game_id FROM games WHERE "
        for var in conditions:
            query += f"{var['header']} {var['conditional']} %s AND "
        query = query[:-5]
        query += f" ORDER BY {order_by} ASC"
        self.cursor.execute(
            query, tuple([condition["value"] for condition in conditions])
        )
        rows = self.cursor.fetchall()
        prev_game_ids = []
        for row in rows:
            prev_ids = self.prev_game_ids(row["game_id"])
            prev_game_ids.append(
                {
                    "game_id": row["game_id"],
                    "prev_game_id_home": prev_ids["home"],
                    "prev_game_id_away": prev_ids["away"],
                }
            )
        return prev_game_ids

    def prev_game_ids(self, game_id):
        return {
            "home": self.team_prev_game_id(game_id, game_id[10:13]),
            "away": self.team_prev_game_id(game_id, game_id[13:]),
        }

    def team_prev_game_id(self, game_id, team):
        self.cursor.execute("SELECT * FROM games WHERE game_id = %s", (game_id))
        rows = self.cursor.fetchall()
        if rows.__len__() == 0:
            return "NA"
        game_date = rows[0]["game_date"]
        season = rows[0]["season"]
        prev_game = "NA"
        self.cursor.execute(
            "SELECT * FROM games WHERE (home_team = %(team)s OR away_team = %(team)s) AND game_date < %(game_date)s AND season = %(season)s ORDER BY game_date DESC LIMIT 1",
            {"team": team, "game_date": game_date, "season": season},
        )
        rows = self.cursor.fetchall()
        if rows.__len__() != 0:
            prev_game = rows[0]["game_id"]
        return prev_game
