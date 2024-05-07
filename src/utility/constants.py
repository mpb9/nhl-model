# Purpose: ALL COMMONLY USED CONSTANTS

# MARK: DATABASE PATHS
DB_PATH = "/databases"
BY_TEAM_DB = DB_PATH + "/BY_TEAM"
MODELS_DB = DB_PATH + "/MODELS"
UTILS_DB = DB_PATH + "/UTILS"
TEMP_DB = DB_PATH + "/TEMP"
TEAM_POWER_RANK_DB = BY_TEAM_DB + "/POWER_RANK"
TEAM_ROLLING_DB = BY_TEAM_DB + "/ROLLING"
TEAM_TRAJECTORY_DB = BY_TEAM_DB + "/TRAJECTORY"

# MARK: SQL QUERIES
DELETE_TEMP_TxG = "DROP TABLE IF EXISTS txg_test"
CREATE_TEMP_TxG = "CREATE TABLE IF NOT EXISTS txg_test (game_id varchar(20) DEFAULT NULL, team varchar(4) DEFAULT NULL, season year(4) DEFAULT NULL, opposingTeam varchar(4) DEFAULT NULL, home_or_away varchar(1) DEFAULT NULL, gameDate date DEFAULT NULL, situation varchar(10) DEFAULT NULL, xGoalsPercentage float DEFAULT NULL, corsiPercentage float DEFAULT NULL, fenwickPercentage float DEFAULT NULL, iceTime float DEFAULT NULL, xOnGoalFor float DEFAULT NULL, xGoalsFor float DEFAULT NULL, xReboundsFor float DEFAULT NULL, xFreezeFor float DEFAULT NULL, xPlayStoppedFor float DEFAULT NULL, xPlayContinuedInZoneFor float DEFAULT NULL, xPlayContinuedOutsideZoneFor float DEFAULT NULL, flurryAdjustedxGoalsFor float DEFAULT NULL, scoreVenueAdjustedxGoalsFor float DEFAULT NULL, flurryScoreVenueAdjustedxGoalsFor float DEFAULT NULL, shotsOnGoalFor int(3) DEFAULT NULL, missedShotsFor int(3) DEFAULT NULL, blockedShotAttemptsFor int(3) DEFAULT NULL, shotAttemptsFor int(3) DEFAULT NULL, goalsFor int(2) DEFAULT NULL, reboundsFor int(3) DEFAULT NULL, reboundGoalsFor int(3) DEFAULT NULL, freezeFor int(3) DEFAULT NULL, playStoppedFor int(3) DEFAULT NULL, playContinuedInZoneFor int(3) DEFAULT NULL, playContinuedOutsideZoneFor int(3) DEFAULT NULL, savedShotsOnGoalFor int(3) DEFAULT NULL, savedUnblockedShotAttemptsFor int(3) DEFAULT NULL, penaltiesFor int(3) DEFAULT NULL, penaltyMinutesFor int(3) DEFAULT NULL, faceOffsWonFor int(3) DEFAULT NULL, hitsFor int(3) DEFAULT NULL, takeawaysFor int(3) DEFAULT NULL, giveawaysFor int(3) DEFAULT NULL, lowDangerShotsFor int(3) DEFAULT NULL, mediumDangerShotsFor int(3) DEFAULT NULL, highDangerShotsFor int(3) DEFAULT NULL, lowDangerxGoalsFor float DEFAULT NULL, mediumDangerxGoalsFor float DEFAULT NULL, highDangerxGoalsFor float DEFAULT NULL, lowDangerGoalsFor int(2) DEFAULT NULL, mediumDangerGoalsFor int(2) DEFAULT NULL, highDangerGoalsFor int(2) DEFAULT NULL, scoreAdjustedShotsAttemptsFor float DEFAULT NULL, unblockedShotAttemptsFor int(3) DEFAULT NULL, scoreAdjustedUnblockedShotAttemptsFor float DEFAULT NULL, dZoneGiveawaysFor int(3) DEFAULT NULL, xGoalsFromxReboundsOfShotsFor float DEFAULT NULL, xGoalsFromActualReboundsOfShotsFor float DEFAULT NULL, reboundxGoalsFor float DEFAULT NULL, totalShotCreditFor float DEFAULT NULL, scoreAdjustedTotalShotCreditFor float DEFAULT NULL, scoreFlurryAdjustedTotalShotCreditFor float DEFAULT NULL, xOnGoalAgainst float DEFAULT NULL, xGoalsAgainst float DEFAULT NULL, xReboundsAgainst float DEFAULT NULL, xFreezeAgainst float DEFAULT NULL, xPlayStoppedAgainst float DEFAULT NULL, xPlayContinuedInZoneAgainst float DEFAULT NULL, xPlayContinuedOutsideZoneAgainst float DEFAULT NULL, flurryAdjustedxGoalsAgainst float DEFAULT NULL, scoreVenueAdjustedxGoalsAgainst float DEFAULT NULL, flurryScoreVenueAdjustedxGoalsAgainst float DEFAULT NULL, shotsOnGoalAgainst int(3) DEFAULT NULL, missedShotsAgainst int(3) DEFAULT NULL, blockedShotAttemptsAgainst int(3) DEFAULT NULL, shotAttemptsAgainst int(3) DEFAULT NULL, goalsAgainst int(3) DEFAULT NULL, reboundsAgainst int(3) DEFAULT NULL, reboundGoalsAgainst int(3) DEFAULT NULL, freezeAgainst int(3) DEFAULT NULL, playStoppedAgainst int(3) DEFAULT NULL, playContinuedInZoneAgainst int(3) DEFAULT NULL, playContinuedOutsideZoneAgainst int(3) DEFAULT NULL, savedShotsOnGoalAgainst int(3) DEFAULT NULL, savedUnblockedShotAttemptsAgainst int(3) DEFAULT NULL, penaltiesAgainst int(3) DEFAULT NULL, penaltyMinutesAgainst int(3) DEFAULT NULL, faceOffsWonAgainst int(3) DEFAULT NULL, hitsAgainst int(3) DEFAULT NULL, takeawaysAgainst int(3) DEFAULT NULL, giveawaysAgainst int(3) DEFAULT NULL, lowDangerShotsAgainst int(3) DEFAULT NULL, mediumDangerShotsAgainst int(3) DEFAULT NULL, highDangerShotsAgainst int(3) DEFAULT NULL, lowDangerxGoalsAgainst float DEFAULT NULL, mediumDangerxGoalsAgainst float NOT NULL, highDangerxGoalsAgainst float DEFAULT NULL, lowDangerGoalsAgainst int(2) DEFAULT NULL, mediumDangerGoalsAgainst int(2) DEFAULT NULL, highDangerGoalsAgainst int(2) DEFAULT NULL, scoreAdjustedShotsAttemptsAgainst float DEFAULT NULL, unblockedShotAttemptsAgainst int(3) DEFAULT NULL, scoreAdjustedUnblockedShotAttemptsAgainst float DEFAULT NULL, dZoneGiveawaysAgainst int(3) DEFAULT NULL, xGoalsFromxReboundsOfShotsAgainst float DEFAULT NULL, xGoalsFromActualReboundsOfShotsAgainst float DEFAULT NULL, reboundxGoalsAgainst float DEFAULT NULL, totalShotCreditAgainst float DEFAULT NULL, scoreAdjustedTotalShotCreditAgainst float DEFAULT NULL, scoreFlurryAdjustedTotalShotCreditAgainst float DEFAULT NULL) ENGINE=MyISAM DEFAULT CHARSET=latin1"
INIT_TEMP_TxG = "INSERT INTO `txg_test` (`game_id`, `team`, `season`, `opposingTeam`, `home_or_away`, `gameDate`, `situation`, `xGoalsPercentage`, `corsiPercentage`, `fenwickPercentage`, `iceTime`, `xOnGoalFor`, `xGoalsFor`, `xReboundsFor`, `xFreezeFor`, `xPlayStoppedFor`, `xPlayContinuedInZoneFor`, `xPlayContinuedOutsideZoneFor`, `flurryAdjustedxGoalsFor`, `scoreVenueAdjustedxGoalsFor`, `flurryScoreVenueAdjustedxGoalsFor`, `shotsOnGoalFor`, `missedShotsFor`, `blockedShotAttemptsFor`, `shotAttemptsFor`, `goalsFor`, `reboundsFor`, `reboundGoalsFor`, `freezeFor`, `playStoppedFor`, `playContinuedInZoneFor`, `playContinuedOutsideZoneFor`, `savedShotsOnGoalFor`, `savedUnblockedShotAttemptsFor`, `penaltiesFor`, `penaltyMinutesFor`, `faceOffsWonFor`, `hitsFor`, `takeawaysFor`, `giveawaysFor`, `lowDangerShotsFor`, `mediumDangerShotsFor`, `highDangerShotsFor`, `lowDangerxGoalsFor`, `mediumDangerxGoalsFor`, `highDangerxGoalsFor`, `lowDangerGoalsFor`, `mediumDangerGoalsFor`, `highDangerGoalsFor`, `scoreAdjustedShotsAttemptsFor`, `unblockedShotAttemptsFor`, `scoreAdjustedUnblockedShotAttemptsFor`, `dZoneGiveawaysFor`, `xGoalsFromxReboundsOfShotsFor`, `xGoalsFromActualReboundsOfShotsFor`, `reboundxGoalsFor`, `totalShotCreditFor`, `scoreAdjustedTotalShotCreditFor`, `scoreFlurryAdjustedTotalShotCreditFor`, `xOnGoalAgainst`, `xGoalsAgainst`, `xReboundsAgainst`, `xFreezeAgainst`, `xPlayStoppedAgainst`, `xPlayContinuedInZoneAgainst`, `xPlayContinuedOutsideZoneAgainst`, `flurryAdjustedxGoalsAgainst`, `scoreVenueAdjustedxGoalsAgainst`, `flurryScoreVenueAdjustedxGoalsAgainst`, `shotsOnGoalAgainst`, `missedShotsAgainst`, `blockedShotAttemptsAgainst`, `shotAttemptsAgainst`, `goalsAgainst`, `reboundsAgainst`, `reboundGoalsAgainst`, `freezeAgainst`, `playStoppedAgainst`, `playContinuedInZoneAgainst`, `playContinuedOutsideZoneAgainst`, `savedShotsOnGoalAgainst`, `savedUnblockedShotAttemptsAgainst`, `penaltiesAgainst`, `penaltyMinutesAgainst`, `faceOffsWonAgainst`, `hitsAgainst`, `takeawaysAgainst`, `giveawaysAgainst`, `lowDangerShotsAgainst`, `mediumDangerShotsAgainst`, `highDangerShotsAgainst`, `lowDangerxGoalsAgainst`, `mediumDangerxGoalsAgainst`, `highDangerxGoalsAgainst`, `lowDangerGoalsAgainst`, `mediumDangerGoalsAgainst`, `highDangerGoalsAgainst`, `scoreAdjustedShotsAttemptsAgainst`, `unblockedShotAttemptsAgainst`, `scoreAdjustedUnblockedShotAttemptsAgainst`, `dZoneGiveawaysAgainst`, `xGoalsFromxReboundsOfShotsAgainst`, `xGoalsFromActualReboundsOfShotsAgainst`, `reboundxGoalsAgainst`, `totalShotCreditAgainst`, `scoreAdjustedTotalShotCreditAgainst`, `scoreFlurryAdjustedTotalShotCreditAgainst`) VALUES ('2023-04-13FLACAR', 'FLA', 2022, 'CAR', 'H', '2023-04-13', '4on5', 0.2125, 0.0769, 0.0909, 428, 0.676, 0.017, 0.032, 0.119, 0.02, 0.242, 0.57, 0.017, 0.017, 0.017, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2, 5, 1, 4, 1, 0, 0, 0.017, 0, 0, 0, 0, 0, 1, 1, 1, 4, 0.007, 0, 0, 0.024, 0.024, 0.024, 7.017, 0.063, 0.582, 1.594, 0.199, 5.007, 2.555, 0.062, 0.063, 0.062, 5, 5, 2, 12, 0, 0, 0, 1, 0, 5, 4, 5, 10, 0, 0, 3, 0, 1, 0, 10, 0, 0, 0.063, 0, 0, 0, 0, 0, 12, 10, 10, 0, 0.137, 0, 0, 0.2, 0.2, 0.199), ('2023-04-13FLACAR', 'CAR', 2022, 'FLA', 'A', '2023-04-13', '4on5', 0.2703, 0.25, 0.25, 120, 0.935, 0.173, 0.083, 0.091, 0.022, 0.268, 0.363, 0.166, 0.173, 0.166, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0.173, 0, 0, 0, 0, 1, 1, 1, 0, 0.018, 0, 0, 0.191, 0.191, 0.183, 2.332, 0.467, 0.228, 0.388, 0.065, 1.181, 0.671, 0.433, 0.467, 0.433, 1, 2, 0, 3, 0, 0, 0, 0, 0, 3, 0, 1, 3, 1, 2, 3, 0, 0, 0, 1, 1, 1, 0.04, 0.167, 0.26, 0, 0, 0, 3, 3, 3, 0, 0.057, 0, 0, 0.524, 0.524, 0.485), ('2023-04-13FLACAR', 'FLA', 2022, 'CAR', 'H', '2023-04-13', '5on4', 0.7297, 0.75, 0.75, 120, 2.332, 0.467, 0.228, 0.388, 0.065, 1.181, 0.671, 0.433, 0.467, 0.433, 1, 2, 0, 3, 0, 0, 0, 0, 0, 3, 0, 1, 3, 1, 2, 3, 0, 0, 0, 1, 1, 1, 0.04, 0.167, 0.26, 0, 0, 0, 3, 3, 3, 0, 0.057, 0, 0, 0.524, 0.524, 0.485, 0.935, 0.173, 0.083, 0.091, 0.022, 0.268, 0.363, 0.166, 0.173, 0.166, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0.173, 0, 0, 0, 0, 1, 1, 1, 0, 0.018, 0, 0, 0.191, 0.191, 0.183), ('2023-04-13FLACAR', 'CAR', 2022, 'FLA', 'A', '2023-04-13', '5on4', 0.7875, 0.9231, 0.9091, 428, 7.017, 0.063, 0.582, 1.594, 0.199, 5.007, 2.555, 0.062, 0.063, 0.062, 5, 5, 2, 12, 0, 0, 0, 1, 0, 5, 4, 5, 10, 0, 0, 3, 0, 1, 0, 10, 0, 0, 0.063, 0, 0, 0, 0, 0, 12, 10, 10, 0, 0.137, 0, 0, 0.2, 0.2, 0.199, 0.676, 0.017, 0.032, 0.119, 0.02, 0.242, 0.57, 0.017, 0.017, 0.017, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2, 5, 1, 4, 1, 0, 0, 0.017, 0, 0, 0, 0, 0, 1, 1, 1, 4, 0.007, 0, 0, 0.024, 0.024, 0.024), ('2023-04-13FLACAR', 'FLA', 2022, 'CAR', 'H', '2023-04-13', '5on5', 0.3759, 0.4123, 0.3882, 2805, 24.815, 2.175, 1.597, 6.836, 0.79, 12.916, 8.686, 2.082, 1.994, 1.909, 22, 11, 14, 47, 3, 2, 0, 5, 0, 9, 14, 19, 30, 4, 8, 26, 25, 5, 10, 24, 6, 3, 0.637, 0.828, 0.709, 2, 1, 0, 42.565, 33, 30.076, 5, 0.334, 0.471, 0.471, 2.038, 1.87, 1.838, 38.213, 3.611, 2.517, 10.042, 1.35, 19.505, 14.976, 3.433, 3.943, 3.753, 28, 24, 15, 67, 4, 5, 1, 6, 1, 19, 17, 24, 48, 3, 6, 20, 14, 5, 6, 40, 6, 6, 1.124, 0.832, 1.655, 3, 0, 1, 74.987, 52, 57.981, 5, 0.53, 1.104, 1.104, 3.037, 3.336, 3.305), ('2023-04-13FLACAR', 'CAR', 2022, 'FLA', 'A', '2023-04-13', '5on5', 0.6241, 0.5877, 0.6118, 2805, 38.213, 3.611, 2.517, 10.042, 1.35, 19.505, 14.976, 3.433, 3.943, 3.753, 28, 24, 15, 67, 4, 5, 1, 6, 1, 19, 17, 24, 48, 3, 6, 20, 14, 5, 6, 40, 6, 6, 1.124, 0.832, 1.655, 3, 0, 1, 74.987, 52, 57.981, 5, 0.53, 1.104, 1.104, 3.037, 3.336, 3.305, 24.815, 2.175, 1.597, 6.836, 0.79, 12.916, 8.686, 2.082, 1.994, 1.909, 22, 11, 14, 47, 3, 2, 0, 5, 0, 9, 14, 19, 30, 4, 8, 26, 25, 5, 10, 24, 6, 3, 0.637, 0.828, 0.709, 2, 1, 0, 42.565, 33, 30.076, 5, 0.334, 0.471, 0.471, 2.038, 1.87, 1.838), ('2023-04-13FLACAR', 'FLA', 2022, 'CAR', 'H', '2023-04-13', 'all', 0.4675, 0.4315, 0.4159, 3600, 35.661, 4.482, 2.806, 9.041, 1.195, 18.332, 11.144, 3.917, 4.301, 3.744, 34, 13, 16, 63, 4, 6, 1, 7, 0, 15, 15, 30, 43, 5, 10, 37, 31, 6, 16, 29, 10, 8, 0.834, 1.329, 2.319, 2, 1, 1, 58.565, 47, 44.076, 9, 0.651, 1.821, 1.821, 3.311, 3.144, 2.923, 48.162, 5.105, 3.23, 11.973, 1.624, 25.412, 18.656, 4.921, 5.438, 5.24, 36, 30, 17, 83, 6, 5, 1, 7, 1, 26, 21, 30, 60, 3, 6, 24, 14, 6, 6, 51, 7, 8, 1.196, 1.005, 2.904, 3, 0, 3, 90.987, 66, 71.981, 5, 0.699, 1.104, 1.104, 4.7, 4.999, 4.96), ('2023-04-13FLACAR', 'CAR', 2022, 'FLA', 'A', '2023-04-13', 'all', 0.5325, 0.5685, 0.5841, 3600, 48.162, 5.105, 3.23, 11.973, 1.624, 25.412, 18.656, 4.921, 5.438, 5.24, 36, 30, 17, 83, 6, 5, 1, 7, 1, 26, 21, 30, 60, 3, 6, 24, 14, 6, 6, 51, 7, 8, 1.196, 1.005, 2.904, 3, 0, 3, 90.987, 66, 71.981, 5, 0.699, 1.104, 1.104, 4.7, 4.999, 4.96, 35.661, 4.482, 2.806, 9.041, 1.195, 18.332, 11.144, 3.917, 4.301, 3.744, 34, 13, 16, 63, 4, 6, 1, 7, 0, 15, 15, 30, 43, 5, 10, 37, 31, 6, 16, 29, 10, 8, 0.834, 1.329, 2.319, 2, 1, 1, 58.565, 47, 44.076, 9, 0.651, 1.821, 1.821, 3.311, 3.144, 2.923), ('2023-04-13FLACAR', 'FLA', 2022, 'CAR', 'H', '2023-04-13', 'other', 0.5915, 0.8, 0.7692, 247, 7.839, 1.823, 0.949, 1.697, 0.321, 3.994, 1.217, 1.385, 1.823, 1.385, 10, 0, 2, 12, 1, 4, 1, 1, 0, 3, 1, 9, 9, 0, 0, 6, 1, 0, 2, 3, 3, 4, 0.139, 0.334, 1.35, 0, 0, 1, 12, 10, 10, 0, 0.252, 1.35, 1.35, 0.725, 0.725, 0.575, 1.997, 1.259, 0.048, 0.246, 0.052, 0.633, 0.762, 1.259, 1.259, 1.259, 3, 0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0.01, 0, 1.249, 0, 0, 2, 3, 3, 3, 0, 0.013, 0, 0, 1.273, 1.273, 1.273), ('2023-04-13FLACAR', 'CAR', 2022, 'FLA', 'A', '2023-04-13', 'other', 0.4085, 0.2, 0.2308, 247, 1.997, 1.259, 0.048, 0.246, 0.052, 0.633, 0.762, 1.259, 1.259, 1.259, 3, 0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0.01, 0, 1.249, 0, 0, 2, 3, 3, 3, 0, 0.013, 0, 0, 1.273, 1.273, 1.273, 7.839, 1.823, 0.949, 1.697, 0.321, 3.994, 1.217, 1.385, 1.823, 1.385, 10, 0, 2, 12, 1, 4, 1, 1, 0, 3, 1, 9, 9, 0, 0, 6, 1, 0, 2, 3, 3, 4, 0.139, 0.334, 1.35, 0, 0, 1, 12, 10, 10, 0, 0.252, 1.35, 1.35, 0.725, 0.725, 0.575)"

# MARK: OPERATORS
CONDITIONALS = ["=", "!=", ">", "<", ">=", "<=", "LIKE"]

# ! RETIRED
CSV_MODEL_PATH = "~/dev/_DATA/bet-nhl-data/_MODELS/"
CSV_DB_PATH = "~/dev/_DATA/bet-nhl-data/"
CSV_TEMP_PATH = "~/dev/_DATA/bet-nhl-data/_TEMP/"

# MARK: NHL TEAMS
NHL_TEAMS = [
    ["ANA", "Anaheim Ducks", "Anaheim", "Ducks"],
    ["ARI", "Arizona Coyotes", "Arizona", "Coyotes"],
    ["BOS", "Boston Bruins", "Boston", "Bruins"],
    ["BUF", "Buffalo Sabres", "Buffalo", "Sabres"],
    ["CAR", "Carolina Hurricanes", "Carolina", "Hurricanes"],
    ["CBJ", "Columbus Blue Jackets", "Columbus", "Blue Jackets"],
    ["CGY", "Calgary Flames", "Calgary", "Flames"],
    ["CHI", "Chicago Blackhawks", "Chicago", "Blackhawks"],
    ["COL", "Colorado Avalanche", "Colorado", "Avalanche"],
    ["DAL", "Dallas Stars", "Dallas", "Stars"],
    ["DET", "Detroit Red Wings", "Detroit", "Red Wings"],
    ["EDM", "Edmonton Oilers", "Edmonton", "Oilers"],
    ["FLA", "Florida Panthers", "Florida", "Panthers"],
    ["LAK", "Los Angeles Kings", "Los Angeles", "Kings"],
    ["MIN", "Minnesota Wild", "Minnesota", "Wild"],
    ["MTL", "Montreal Canadiens", "Montreal", "Canadiens"],
    ["NJD", "New Jersey Devils", "New Jersey", "Devils"],
    ["NSH", "Nashville Predators", "Nashville", "Predators"],
    ["NYI", "New York Islanders", "New York", "Islanders"],
    ["NYR", "New York Rangers", "New York", "Rangers"],
    ["OTT", "Ottawa Senators", "Ottawa", "Senators"],
    ["PHI", "Philadelphia Flyers", "Philadelphia", "Flyers"],
    ["PIT", "Pittsburgh Penguins", "Pittsburgh", "Penguins"],
    ["SEA", "Seattle Kraken", "Seattle", "Kraken"],
    ["SJS", "San Jose Sharks", "San Jose", "Sharks"],
    ["STL", "St Louis Blues", "St. Louis", "Blues"],
    ["TBL", "Tampa Bay Lightning", "Tampa Bay", "Lightning"],
    ["TOR", "Toronto Maple Leafs", "Toronto", "Maple Leafs"],
    ["VAN", "Vancouver Canucks", "Vancouver", "Canucks"],
    ["VGK", "Vegas Golden Knights", "Vegas", "Golden Knights"],
    ["WPG", "Winnipeg Jets", "Winnipeg", "Jets"],
    ["WSH", "Washington Capitals", "Washington", "Capitals"],
    ["ATL", "Atlanta Thrashers", "Atlanta", "Thrashers"],
]

# MARK: SPECIAL COLS
IGNORED_COLS = [
    "game_id",
    "team",
    "opp_team",
    "season",
    "next_game_id",
    "game_date",
    "situation",
    "game_time",
]
DUPLICATE_COLS = [
    "opp_corsiPercentage",
    "opp_fenwickPercentage",
    "opp_xGoalsPercentage",
]

# MARK: PER_GAME COLS
PG_COLS = (
    [
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
        "penaltyMinutesFor",
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
        "penaltyMinutesAgainst",
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
    ],
)
