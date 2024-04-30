import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
from db_connect import get_db_connection
from sklearn.linear_model import LinearRegression
from nhl_data import NHLData

""" from constants import CREATE_TEMP_TxG
from constants import INIT_TEMP_TxG
from constants import DELETE_TEMP_TxG """

connect = get_db_connection()
cursor = connect.cursor(pymysql.cursors.DictCursor)

query = "SELECT game_id FROM `games` WHERE season = 2022 "
query += "AND game_id NOT IN (SELECT game_id FROM team_x_game_even WHERE season = 2022)"
cursor.execute(query)
rows = cursor.fetchall()
df = pd.DataFrame(rows)
print(df)


def reset():
    cursor.execute(DELETE_TEMP_TxG)
    cursor.execute(CREATE_TEMP_TxG)
    cursor.execute(INIT_TEMP_TxG)


def get_table(home_or_away):
    data = NHLData.conditional_data(
        "txg_test",
        [{"header": "home_or_away", "conditional": "=", "value": home_or_away}],
    )
    return data


def first_update_values():
    # ! ADD new values
    # opp_xGoalsPercentage, opp_corsiPercentage, opp_fenwickPercentage
    query = "ALTER TABLE `txg_test` ADD `opp_xGoalsPercentage` FLOAT NOT NULL AFTER `fenwickPercentage`, ADD `opp_corsiPercentage` INT NOT NULL AFTER `opp_xGoalsPercentage`, ADD `opp_fenwickPercentage` FLOAT NOT NULL AFTER `opp_corsiPercentage`"
    cursor.execute(query)
    query = "UPDATE `txg_test` SET `opp_xGoalsPercentage` = 1 - `xGoalsPercentage`, `opp_corsiPercentage` = 1 - `corsiPercentage`, `opp_fenwickPercentage` = 1 - `fenwickPercentage`"
    cursor.execute(query)

    # ! CONFIGURE situation
    query = "UPDATE `txg_test` SET `situation` = 'H_KILL' WHERE home_or_away = 'H' AND situation = '4on5'"
    cursor.execute(query)
    query = "UPDATE `txg_test` SET `situation` = 'A_KILL' WHERE home_or_away = 'A' AND situation = '4on5'"
    cursor.execute(query)
    query = "UPDATE `txg_test` SET `situation` = 'H_PP' WHERE home_or_away = 'H' AND situation = '5on4'"
    cursor.execute(query)
    query = "UPDATE `txg_test` SET `situation` = 'A_PP' WHERE home_or_away = 'A' AND situation = '5on4'"
    cursor.execute(query)

    # ! CONTINUE WITH THIS


def second_change_vars():
    return 0
