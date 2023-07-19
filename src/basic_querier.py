import sys
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

sys.path.append("/get_data")
from get_data.nhl_data import NHLData
from get_data.utility_data import UtilityData
from constants import CONDITIONALS

nhl_data = NHLData()
utility_data = UtilityData()

connect = pymysql.connect(
    host="localhost", user="mpb9", password="9Chester!", database="bet_nhl"
)
cursor = connect.cursor(pymysql.cursors.DictCursor)

engine = sqlalchemy.create_engine("mysql+pymysql://mpb9:9Chester!@localhost/bet_nhl")
connection = engine.connect()
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)

table_name = "team_x_game_even"
table = metadata.tables[table_name]
columns = sqlalchemy.Table(table_name, metadata, autoload=True).columns

table_cols = [
    "game_id",
    "team",
    "season",
    "opposingTeam",
    "home_or_away",
    "gameDate",
    "situation",
    "iceTime",
    "xGoalsPercentageFor",
    "xGoalsPercentageAgainst",
    "corsiPercentageFor",
    "corsiPercentageAgainst",
    "fenwickPercentageFor",
    "fenwickPercentageAgainst",
    "xOnGoalFor",
    "xGoalsFor",
    "xReboundsFor",
    "xFreezeFor",
    "xPlayStoppedFor",
    "xPlayContinuedInZoneFor",
    "xPlayContinuedOutsideZoneFor",
    "flurryAdjustedxGoalsFor",
    "scoreVenueAdjustedxGoalsFor",
    "flurryScoreVenueAdjustedxGoalsFor",
    "shotsOnGoalFor",
    "missedShotsFor",
    "blockedShotAttemptsFor",
    "shotAttemptsFor",
    "goalsFor",
    "reboundsFor",
    "reboundGoalsFor",
    "freezeFor",
    "playStoppedFor",
    "playContinuedInZoneFor",
    "playContinuedOutsideZoneFor",
    "savedShotsOnGoalFor",
    "savedUnblockedShotAttemptsFor",
    "penaltiesFor",
    "penalityMinutesFor",
    "faceOffsWonFor",
    "hitsFor",
    "takeawaysFor",
    "giveawaysFor",
    "lowDangerShotsFor",
    "mediumDangerShotsFor",
    "highDangerShotsFor",
    "lowDangerxGoalsFor",
    "mediumDangerxGoalsFor",
    "highDangerxGoalsFor",
    "lowDangerGoalsFor",
    "mediumDangerGoalsFor",
    "highDangerGoalsFor",
    "scoreAdjustedShotsAttemptsFor",
    "unblockedShotAttemptsFor",
    "scoreAdjustedUnblockedShotAttemptsFor",
    "dZoneGiveawaysFor",
    "xGoalsFromxReboundsOfShotsFor",
    "xGoalsFromActualReboundsOfShotsFor",
    "reboundxGoalsFor",
    "totalShotCreditFor",
    "scoreAdjustedTotalShotCreditFor",
    "scoreFlurryAdjustedTotalShotCreditFor",
    "xOnGoalAgainst",
    "xGoalsAgainst",
    "xReboundsAgainst",
    "xFreezeAgainst",
    "xPlayStoppedAgainst",
    "xPlayContinuedInZoneAgainst",
    "xPlayContinuedOutsideZoneAgainst",
    "flurryAdjustedxGoalsAgainst",
    "scoreVenueAdjustedxGoalsAgainst",
    "flurryScoreVenueAdjustedxGoalsAgainst",
    "shotsOnGoalAgainst",
    "missedShotsAgainst",
    "blockedShotAttemptsAgainst",
    "shotAttemptsAgainst",
    "goalsAgainst",
    "reboundsAgainst",
    "reboundGoalsAgainst",
    "freezeAgainst",
    "playStoppedAgainst",
    "playContinuedInZoneAgainst",
    "playContinuedOutsideZoneAgainst",
    "savedShotsOnGoalAgainst",
    "savedUnblockedShotAttemptsAgainst",
    "penaltiesAgainst",
    "penalityMinutesAgainst",
    "faceOffsWonAgainst",
    "hitsAgainst",
    "takeawaysAgainst",
    "giveawaysAgainst",
    "lowDangerShotsAgainst",
    "mediumDangerShotsAgainst",
    "highDangerShotsAgainst",
    "lowDangerxGoalsAgainst",
    "mediumDangerxGoalsAgainst",
    "highDangerxGoalsAgainst",
    "lowDangerGoalsAgainst",
    "mediumDangerGoalsAgainst",
    "highDangerGoalsAgainst",
    "scoreAdjustedShotsAttemptsAgainst",
    "unblockedShotAttemptsAgainst",
    "scoreAdjustedUnblockedShotAttemptsAgainst",
    "dZoneGiveawaysAgainst",
    "xGoalsFromxReboundsOfShotsAgainst",
    "xGoalsFromActualReboundsOfShotsAgainst",
    "reboundxGoalsAgainst",
    "totalShotCreditAgainst",
    "scoreAdjustedTotalShotCreditAgainst",
    "scoreFlurryAdjustedTotalShotCreditAgainst",
]

# info: BASIC QUERIER
query = "INSERT INTO team_x_game_even (game_id, team, season, opposingTeam, home_or_away, gameDate, situation, iceTime, xGoalsPercentageFor, xGoalsPercentageAgainst, corsiPercentageFor, corsiPercentageAgainst, fenwickPercentageFor, fenwickPercentageAgainst, xOnGoalFor, xGoalsFor, xReboundsFor, xFreezeFor, xPlayStoppedFor, xPlayContinuedInZoneFor, xPlayContinuedOutsideZoneFor, flurryAdjustedxGoalsFor, scoreVenueAdjustedxGoalsFor, flurryScoreVenueAdjustedxGoalsFor, shotsOnGoalFor, missedShotsFor, blockedShotAttemptsFor, shotAttemptsFor, goalsFor, reboundsFor, reboundGoalsFor, freezeFor, playStoppedFor, playContinuedInZoneFor, playContinuedOutsideZoneFor, savedShotsOnGoalFor, savedUnblockedShotAttemptsFor, penaltiesFor, penalityMinutesFor, faceOffsWonFor, hitsFor, takeawaysFor, giveawaysFor, lowDangerShotsFor, mediumDangerShotsFor, highDangerShotsFor, lowDangerxGoalsFor, mediumDangerxGoalsFor, highDangerxGoalsFor, lowDangerGoalsFor, mediumDangerGoalsFor, highDangerGoalsFor, scoreAdjustedShotsAttemptsFor, unblockedShotAttemptsFor, scoreAdjustedUnblockedShotAttemptsFor, dZoneGiveawaysFor, xGoalsFromxReboundsOfShotsFor, xGoalsFromActualReboundsOfShotsFor, reboundxGoalsFor, totalShotCreditFor, scoreAdjustedTotalShotCreditFor, scoreFlurryAdjustedTotalShotCreditFor, xOnGoalAgainst, xGoalsAgainst, xReboundsAgainst, xFreezeAgainst, xPlayStoppedAgainst, xPlayContinuedInZoneAgainst, xPlayContinuedOutsideZoneAgainst, flurryAdjustedxGoalsAgainst, scoreVenueAdjustedxGoalsAgainst, flurryScoreVenueAdjustedxGoalsAgainst, shotsOnGoalAgainst, missedShotsAgainst, blockedShotAttemptsAgainst, shotAttemptsAgainst, goalsAgainst, reboundsAgainst, reboundGoalsAgainst, freezeAgainst, playStoppedAgainst, playContinuedInZoneAgainst, playContinuedOutsideZoneAgainst, savedShotsOnGoalAgainst, savedUnblockedShotAttemptsAgainst, penaltiesAgainst, penalityMinutesAgainst, faceOffsWonAgainst, hitsAgainst, takeawaysAgainst, giveawaysAgainst, lowDangerShotsAgainst, mediumDangerShotsAgainst, highDangerShotsAgainst, lowDangerxGoalsAgainst, mediumDangerxGoalsAgainst, highDangerxGoalsAgainst, lowDangerGoalsAgainst, mediumDangerGoalsAgainst,"
query += " highDangerGoalsAgainst, scoreAdjustedShotsAttemptsAgainst, unblockedShotAttemptsAgainst, scoreAdjustedUnblockedShotAttemptsAgainst, dZoneGiveawaysAgainst, xGoalsFromxReboundsOfShotsAgainst, xGoalsFromActualReboundsOfShotsAgainst, reboundxGoalsAgainst, totalShotCreditAgainst, scoreAdjustedTotalShotCreditAgainst, scoreFlurryAdjustedTotalShotCreditAgainst)"
query += " SELECT game_id, opposingTeam AS team, season, team AS opposingTeam, CASE WHEN home_or_away = 'H' THEN 'A' ELSE 'H' END AS home_or_away, gameDate, situation, iceTime,"
query += " xGoalsPercentageAgainst AS xGoalsPercentageFor, xGoalsPercentageFor AS xGoalsPercentageAgainst, corsiPercentageAgainst AS corsiPercentageFor, corsiPercentageFor AS corsiPercentageAgainst, fenwickPercentageAgainst AS fenwickPercentageFor, fenwickPercentageFor AS fenwickPercentageAgainst, xOnGoalAgainst AS xOnGoalFor, xGoalsAgainst AS xGoalsFor, xReboundsAgainst AS xReboundsFor, xFreezeAgainst AS xFreezeFor, xPlayStoppedAgainst AS xPlayStoppedFor, xPlayContinuedInZoneAgainst AS xPlayContinuedInZoneFor, xPlayContinuedOutsideZoneAgainst AS xPlayContinuedOutsideZoneFor, flurryAdjustedxGoalsAgainst AS flurryAdjustedxGoalsFor, scoreVenueAdjustedxGoalsAgainst AS scoreVenueAdjustedxGoalsFor, flurryScoreVenueAdjustedxGoalsAgainst AS flurryScoreVenueAdjustedxGoalsFor, shotsOnGoalAgainst AS shotsOnGoalFor, missedShotsAgainst AS missedShotsFor, blockedShotAttemptsAgainst AS blockedShotAttemptsFor, shotAttemptsAgainst AS shotAttemptsFor, goalsAgainst AS goalsFor, reboundsAgainst AS reboundsFor, reboundGoalsAgainst AS reboundGoalsFor, freezeAgainst AS freezeFor, playStoppedAgainst AS playStoppedFor, playContinuedInZoneAgainst AS playContinuedInZoneFor, playContinuedOutsideZoneAgainst AS playContinuedOutsideZoneFor, savedShotsOnGoalAgainst AS savedShotsOnGoalFor, savedUnblockedShotAttemptsAgainst AS savedUnblockedShotAttemptsFor, penaltiesAgainst AS penaltiesFor, penalityMinutesAgainst AS penalityMinutesFor, faceOffsWonAgainst AS faceOffsWonFor, hitsAgainst AS hitsFor, takeawaysAgainst AS takeawaysFor, giveawaysAgainst AS giveawaysFor, lowDangerShotsAgainst AS"
query += " lowDangerShotsFor, mediumDangerShotsAgainst AS mediumDangerShotsFor, highDangerShotsAgainst AS highDangerShotsFor, lowDangerxGoalsAgainst AS lowDangerxGoalsFor, mediumDangerxGoalsAgainst AS mediumDangerxGoalsFor, highDangerxGoalsAgainst AS highDangerxGoalsFor, lowDangerGoalsAgainst AS lowDangerGoalsFor, mediumDangerGoalsAgainst AS mediumDangerGoalsFor, highDangerGoalsAgainst AS highDangerGoalsFor, scoreAdjustedShotsAttemptsAgainst AS scoreAdjustedShotsAttemptsFor, unblockedShotAttemptsAgainst AS unblockedShotAttemptsFor, scoreAdjustedUnblockedShotAttemptsAgainst AS scoreAdjustedUnblockedShotAttemptsFor, dZoneGiveawaysAgainst AS dZoneGiveawaysFor, xGoalsFromxReboundsOfShotsAgainst AS xGoalsFromxReboundsOfShotsFor, xGoalsFromActualReboundsOfShotsAgainst AS xGoalsFromActualReboundsOfShotsFor, reboundxGoalsAgainst AS reboundxGoalsFor, totalShotCreditAgainst AS totalShotCreditFor, scoreAdjustedTotalShotCreditAgainst AS scoreAdjustedTotalShotCreditFor, scoreFlurryAdjustedTotalShotCreditAgainst AS scoreFlurryAdjustedTotalShotCreditFor, xOnGoalFor AS xOnGoalAgainst, xGoalsFor AS xGoalsAgainst, xReboundsFor AS xReboundsAgainst, xFreezeFor AS xFreezeAgainst, xPlayStoppedFor AS xPlayStoppedAgainst, xPlayContinuedInZoneFor AS xPlayContinuedInZoneAgainst, xPlayContinuedOutsideZoneFor AS xPlayContinuedOutsideZoneAgainst, flurryAdjustedxGoalsFor AS flurryAdjustedxGoalsAgainst, scoreVenueAdjustedxGoalsFor AS"
query += " scoreVenueAdjustedxGoalsAgainst, flurryScoreVenueAdjustedxGoalsFor AS flurryScoreVenueAdjustedxGoalsAgainst, shotsOnGoalFor AS shotsOnGoalAgainst, missedShotsFor AS missedShotsAgainst, blockedShotAttemptsFor AS blockedShotAttemptsAgainst, shotAttemptsFor AS shotAttemptsAgainst, goalsFor AS goalsAgainst, reboundsFor AS reboundsAgainst, reboundGoalsFor AS reboundGoalsAgainst, freezeFor AS freezeAgainst, playStoppedFor AS playStoppedAgainst, playContinuedInZoneFor AS playContinuedInZoneAgainst, playContinuedOutsideZoneFor AS playContinuedOutsideZoneAgainst, savedShotsOnGoalFor AS savedShotsOnGoalAgainst, savedUnblockedShotAttemptsFor AS savedUnblockedShotAttemptsAgainst, penaltiesFor AS penaltiesAgainst, penalityMinutesFor AS penalityMinutesAgainst, faceOffsWonFor AS faceOffsWonAgainst, hitsFor AS hitsAgainst, takeawaysFor AS takeawaysAgainst, giveawaysFor AS giveawaysAgainst, lowDangerShotsFor AS lowDangerShotsAgainst, mediumDangerShotsFor AS mediumDangerShotsAgainst, highDangerShotsFor AS highDangerShotsAgainst, lowDangerxGoalsFor AS lowDangerxGoalsAgainst, mediumDangerxGoalsFor AS mediumDangerxGoalsAgainst, highDangerxGoalsFor AS highDangerxGoalsAgainst, lowDangerGoalsFor AS lowDangerGoalsAgainst, mediumDangerGoalsFor AS mediumDangerGoalsAgainst, highDangerGoalsFor AS highDangerGoalsAgainst, scoreAdjustedShotsAttemptsFor AS scoreAdjustedShotsAttemptsAgainst, unblockedShotAttemptsFor AS unblockedShotAttemptsAgainst, scoreAdjustedUnblockedShotAttemptsFor AS scoreAdjustedUnblockedShotAttemptsAgainst, dZoneGiveawaysFor AS dZoneGiveawaysAgainst, xGoalsFromxReboundsOfShotsFor AS xGoalsFromxReboundsOfShotsAgainst, xGoalsFromActualReboundsOfShotsFor AS xGoalsFromActualReboundsOfShotsAgainst, reboundxGoalsFor AS reboundxGoalsAgainst, totalShotCreditFor AS totalShotCreditAgainst, scoreAdjustedTotalShotCreditFor AS scoreAdjustedTotalShotCreditAgainst, scoreFlurryAdjustedTotalShotCreditFor AS scoreFlurryAdjustedTotalShotCreditAgainst FROM team_x_game_even"
query += " WHERE (opposingTeam, game_id) NOT IN (select team, game_id from team_x_game_even);"
cursor.execute(query)
rows = cursor.fetchall()

df = pd.DataFrame(rows)


# info: RENAME COLUMN (String Replace)
""" for column in columns:
    column_name = column.name
    new_column_name = column_name.replace("For", "Home")

    if column_name != new_column_name & column_name.contains("For"):
        # Generate the ALTER TABLE statement
        alter_table_statement = f"ALTER TABLE {table_name} CHANGE COLUMN {column_name} {new_column_name} {column.type}"

        connection.execute(alter_table_statement)

    column_name = column.name
    new_column_name = column_name.replace("Against", "Away")
    if column_name != new_column_name & column_name.contains("Against"):
        # Generate the ALTER TABLE statement
        alter_table_statement = f"ALTER TABLE {table_name} CHANGE COLUMN {column_name} {new_column_name} {column.type}"
        connection.execute(alter_table_statement) """

# info: DELETE ROW
""" table_name = "team_x_game_even"
condition = "game_id = 2020020001"
delete_statement = f"DELETE FROM {table_name} WHERE {condition}"
connection.execute(delete_statement) """


# ! rows where opposingTeam doesn't have a row in...
# team_x_game_even_2022: 300 ...all contain NJD, LAK, SJS, TBL
# team_x_game_even_2021: 298 ...all contain NJD, LAK, SJS, TBL

# info: add missing Team rows (team_x_game_missing)
# """
table_name = "team_x_game_even_missing"
new_table_name = "team_x_game_even_all"

query = f"SELECT * FROM {table_name};"
cursor.execute(query)
rows = cursor.fetchall()

query = f"CREATE TABLE {new_table_name} AS SELECT "
query += f"game_id, team AS home_team, season, opposingTeam AS away_team, gameDate, situation, iceTime, "
for table_col in table_cols:
    if table_col.find("For") != -1:
        updated_col = table_col.replace("For", "Home")
        query += f"{table_col} AS {updated_col}, "
    elif table_col.find("Against") != -1:
        updated_col = table_col.replace("Against", "Away")
        query += f"{table_col} AS {updated_col}, "
query = query[:-2]
query += f" FROM {table_name}"
query += f" WHERE home_or_away = 'H';"
print("")
print("")
print("")
print(query)


for row in rows:
    if row["home_or_away"] == "H":
        for table_col in table_cols:
            if table_col.find("For") != -1:
                updated_col = table_col.replace("Home", "For")
                query += f"{updated_col} AS {table_col}, "
            elif table_col.find("Against") != -1:
                updated_col = table_col.replace("Away", "Against")
                query += f"{updated_col} AS {table_col}, "
            else:
                query += f"{table_col}, "
query = query[:-2]
query += f" FROM {table_name};"
""""""
