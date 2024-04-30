-- EXPORT GAMES_YYYY:
SELECT * from bet_nhl.games 
WHERE season = YYYY;

-- CREATE new oxg table & EXPORT ODDS_X_GAME_YYYY:
CREATE TABLE oxg_YYYY AS
SELECT * FROM betting.odds_x_game 
WHERE (betting.odds_x_game.game_id) IN (
  SELECT bet_nhl.games.game_id FROM bet_nhl.games 
  WHERE bet_nhl.games.season = YYYY
) ORDER BY betting.odds_x_game.game_id ASC;

-- TEAM_X_GAME_SIT_YYYY:
-- TEST if missing any team specific rows
SELECT DISTINCT COUNT(bet_nhl.team_x_game_SIT_all.game_id) FROM bet_nhl.team_x_game_SIT_all
WHERE bet_nhl.team_x_game_SIT_all.season = YYYY
GROUP BY bet_nhl.team_x_game_SIT_all.game_id
ORDER BY COUNT(bet_nhl.team_x_game_SIT_all.game_id) ASC
LIMIT 1;

-- if TEST = 1, need to add missing team specific rows:


-- if TEST = 2, CREATE new txg table & EXPORT:
CREATE TABLE bet_nhl.txg_SIT_YYYY AS 
SELECT game_id, team AS home_team, season, opposingTeam AS away_team, game_date, situation, iceTime, xGoalsPercentageFor AS xGoalsPercentageHome, xGoalsPercentageAgainst AS xGoalsPercentageAway, corsiPercentageFor AS corsiPercentageHome, corsiPercentageAgainst AS corsiPercentageAway, fenwickPercentageFor AS fenwickPercentageHome, fenwickPercentageAgainst AS fenwickPercentageAway, xOnGoalFor AS xOnGoalHome, xGoalsFor AS xGoalsHome, xReboundsFor AS xReboundsHome, xFreezeFor AS xFreezeHome, xPlayStoppedFor AS xPlayStoppedHome, xPlayContinuedInZoneFor 
AS xPlayContinuedInZoneHome, xPlayContinuedOutsideZoneFor AS xPlayContinuedOutsideZoneHome, flurryAdjustedxGoalsFor AS flurryAdjustedxGoalsHome, scoreVenueAdjustedxGoalsFor AS scoreVenueAdjustedxGoalsHome, flurryScoreVenueAdjustedxGoalsFor AS flurryScoreVenueAdjustedxGoalsHome, shotsOnGoalFor AS shotsOnGoalHome, missedShotsFor AS missedShotsHome, blockedShotAttemptsFor AS blockedShotAttemptsHome, shotAttemptsFor AS shotAttemptsHome, goalsFor AS goalsHome, reboundsFor 
AS reboundsHome, reboundGoalsFor AS reboundGoalsHome, freezeFor AS freezeHome, playStoppedFor AS playStoppedHome, playContinuedInZoneFor AS playContinuedInZoneHome, playContinuedOutsideZoneFor AS playContinuedOutsideZoneHome, savedShotsOnGoalFor AS savedShotsOnGoalHome, savedUnblockedShotAttemptsFor AS savedUnblockedShotAttemptsHome, penaltiesFor AS penaltiesHome, penalityMinutesFor AS penalityMinutesHome, faceOffsWonFor AS faceOffsWonHome, hitsFor AS hitsHome, takeawaysFor AS takeawaysHome, giveawaysFor AS giveawaysHome, lowDangerShotsFor AS lowDangerShotsHome, mediumDangerShotsFor 
AS mediumDangerShotsHome, highDangerShotsFor AS highDangerShotsHome, lowDangerxGoalsFor AS lowDangerxGoalsHome, mediumDangerxGoalsFor AS mediumDangerxGoalsHome, highDangerxGoalsFor AS highDangerxGoalsHome, lowDangerGoalsFor AS lowDangerGoalsHome, mediumDangerGoalsFor AS mediumDangerGoalsHome, highDangerGoalsFor AS highDangerGoalsHome, scoreAdjustedShotsAttemptsFor AS scoreAdjustedShotsAttemptsHome, unblockedShotAttemptsFor AS unblockedShotAttemptsHome, scoreAdjustedUnblockedShotAttemptsFor AS scoreAdjustedUnblockedShotAttemptsHome, dZoneGiveawaysFor AS dZoneGiveawaysHome, xGoalsFromxReboundsOfShotsFor AS xGoalsFromxReboundsOfShotsHome, xGoalsFromActualReboundsOfShotsFor AS xGoalsFromActualReboundsOfShotsHome, reboundxGoalsFor AS reboundxGoalsHome, totalShotCreditFor AS totalShotCreditHome, scoreAdjustedTotalShotCreditFor AS scoreAdjustedTotalShotCreditHome, scoreFlurryAdjustedTotalShotCreditFor AS scoreFlurryAdjustedTotalShotCreditHome, xOnGoalAgainst AS xOnGoalAway, xGoalsAgainst AS xGoalsAway, xReboundsAgainst AS xReboundsAway, xFreezeAgainst AS xFreezeAway, xPlayStoppedAgainst AS xPlayStoppedAway, xPlayContinuedInZoneAgainst AS xPlayContinuedInZoneAway, xPlayContinuedOutsideZoneAgainst AS xPlayContinuedOutsideZoneAway, flurryAdjustedxGoalsAgainst AS flurryAdjustedxGoalsAway, scoreVenueAdjustedxGoalsAgainst AS scoreVenueAdjustedxGoalsAway, flurryScoreVenueAdjustedxGoalsAgainst AS flurryScoreVenueAdjustedxGoalsAway, shotsOnGoalAgainst AS shotsOnGoalAway, missedShotsAgainst AS missedShotsAway, blockedShotAttemptsAgainst AS blockedShotAttemptsAway, shotAttemptsAgainst AS shotAttemptsAway, goalsAgainst AS goalsAway, reboundsAgainst AS reboundsAway, reboundGoalsAgainst AS reboundGoalsAway, freezeAgainst AS freezeAway, playStoppedAgainst AS playStoppedAway, playContinuedInZoneAgainst AS playContinuedInZoneAway, playContinuedOutsideZoneAgainst AS playContinuedOutsideZoneAway, savedShotsOnGoalAgainst AS savedShotsOnGoalAway, savedUnblockedShotAttemptsAgainst AS savedUnblockedShotAttemptsAway, penaltiesAgainst AS penaltiesAway, penalityMinutesAgainst AS penalityMinutesAway, faceOffsWonAgainst AS faceOffsWonAway, hitsAgainst AS hitsAway, takeawaysAgainst AS takeawaysAway, giveawaysAgainst AS giveawaysAway, lowDangerShotsAgainst AS lowDangerShotsAway, mediumDangerShotsAgainst AS mediumDangerShotsAway, highDangerShotsAgainst AS 
highDangerShotsAway, lowDangerxGoalsAgainst AS lowDangerxGoalsAway, mediumDangerxGoalsAgainst AS mediumDangerxGoalsAway, highDangerxGoalsAgainst AS highDangerxGoalsAway, lowDangerGoalsAgainst AS lowDangerGoalsAway, mediumDangerGoalsAgainst AS mediumDangerGoalsAway, highDangerGoalsAgainst AS highDangerGoalsAway, scoreAdjustedShotsAttemptsAgainst AS scoreAdjustedShotsAttemptsAway, unblockedShotAttemptsAgainst AS unblockedShotAttemptsAway, scoreAdjustedUnblockedShotAttemptsAgainst AS scoreAdjustedUnblockedShotAttemptsAway, dZoneGiveawaysAgainst AS dZoneGiveawaysAway, xGoalsFromxReboundsOfShotsAgainst AS xGoalsFromxReboundsOfShotsAway, xGoalsFromActualReboundsOfShotsAgainst AS xGoalsFromActualReboundsOfShotsAway, reboundxGoalsAgainst AS reboundxGoalsAway, totalShotCreditAgainst AS totalShotCreditAway, scoreAdjustedTotalShotCreditAgainst AS scoreAdjustedTotalShotCreditAway, scoreFlurryAdjustedTotalShotCreditAgainst AS scoreFlurryAdjustedTotalShotCreditAway 
FROM bet_nhl.team_x_game_SIT_all
WHERE home_or_away = 'H'
AND situation = SIT
AND season = YYYY;

