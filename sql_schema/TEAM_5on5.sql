create or replace TABLE DUMPNCHASE.PUBLIC.TEAM_5ON5 (
	ID VARCHAR(9) NOT NULL,
	GAME_ID VARCHAR(16),
	TEAM VARCHAR(3),
	OPP_TEAM VARCHAR(3),
	SEASON NUMBER(4,0),
	GAME_NUMBER NUMBER(2,0),
	NEXT_GAME_ID VARCHAR(16),
	SCORE NUMBER(2,0),
	OPP_SCORE NUMBER(2,0),
	WIN NUMBER(1,0),
	REG_WIN NUMBER(1,0),
	OVERTIME NUMBER(1,0),
	ODDS NUMBER(6,5),
	OPP_ODDS NUMBER(6,5),
	OT_ODDS NUMBER(6,5),
	SITUATION VARCHAR(8),
	GAME_DATE DATE,
	GAME_TIME TIME(9),
	REST NUMBER(4,1),
	IS_HOME NUMBER(1,0),
	ICETIME NUMBER(4,0),
	XGOALSPERCENTAGE NUMBER(5,4),
	CORSIPERCENTAGE NUMBER(5,4),
	FENWICKPERCENTAGE NUMBER(5,4),
	OPP_XONGOAL NUMBER(5,3),
	OPP_XGOALS NUMBER(5,3),
	OPP_XREBOUNDS NUMBER(5,3),
	OPP_XFREEZE NUMBER(5,3),
	OPP_XPLAYSTOPPED NUMBER(5,3),
	OPP_XPLAYCONTINUEDINZONE NUMBER(5,3),
	OPP_XPLAYCONTINUEDOUTSIDEZONE NUMBER(5,3),
	OPP_FLURRYADJUSTEDXGOALS NUMBER(5,3),
	OPP_SCOREVENUEADJUSTEDXGOALS NUMBER(5,3),
	OPP_FLURRYSCOREVENUEADJUSTEDXGOALS NUMBER(5,3),
	OPP_SHOTSONGOAL NUMBER(3,0),
	OPP_MISSEDSHOTS NUMBER(3,0),
	OPP_BLOCKEDSHOTATTEMPTS NUMBER(3,0),
	OPP_SHOTATTEMPTS NUMBER(3,0),
	OPP_GOALS NUMBER(3,0),
	OPP_REBOUNDS NUMBER(3,0),
	OPP_REBOUNDGOALS NUMBER(3,0),
	OPP_FREEZE NUMBER(3,0),
	OPP_PLAYSTOPPED NUMBER(3,0),
	OPP_PLAYCONTINUEDINZONE NUMBER(3,0),
	OPP_PLAYCONTINUEDOUTSIDEZONE NUMBER(3,0),
	OPP_SAVEDSHOTSONGOAL NUMBER(3,0),
	OPP_SAVEDUNBLOCKEDSHOTATTEMPTS NUMBER(3,0),
	OPP_PENALTIES NUMBER(3,0),
	OPP_PENALITYMINUTES NUMBER(3,0),
	OPP_FACEOFFSWON NUMBER(3,0),
	OPP_HITS NUMBER(3,0),
	OPP_TAKEAWAYS NUMBER(3,0),
	OPP_GIVEAWAYS NUMBER(3,0),
	OPP_LOWDANGERSHOTS NUMBER(3,0),
	OPP_MEDIUMDANGERSHOTS NUMBER(3,0),
	OPP_HIGHDANGERSHOTS NUMBER(3,0),
	OPP_LOWDANGERXGOALS NUMBER(5,3),
	OPP_MEDIUMDANGERXGOALS NUMBER(5,3),
	OPP_HIGHDANGERXGOALS NUMBER(5,3),
	OPP_LOWDANGERGOALS NUMBER(3,0),
	OPP_MEDIUMDANGERGOALS NUMBER(3,0),
	OPP_HIGHDANGERGOALS NUMBER(3,0),
	OPP_SCOREADJUSTEDSHOTSATTEMPTS NUMBER(5,3),
	OPP_UNBLOCKEDSHOTATTEMPTS NUMBER(3,0),
	OPP_SCOREADJUSTEDUNBLOCKEDSHOTATTEMPTS NUMBER(5,3),
	OPP_DZONEGIVEAWAYS NUMBER(3,0),
	OPP_XGOALSFROMXREBOUNDSOFSHOTS NUMBER(5,3),
	OPP_XGOALSFROMACTUALREBOUNDSOFSHOTS NUMBER(5,3),
	OPP_REBOUNDXGOALS NUMBER(5,3),
	OPP_TOTALSHOTCREDIT NUMBER(5,3),
	OPP_SCOREADJUSTEDTOTALSHOTCREDIT NUMBER(5,3),
	OPP_SCOREFLURRYADJUSTEDTOTALSHOTCREDIT NUMBER(5,3),
	XONGOAL NUMBER(5,3),
	XGOALS NUMBER(5,3),
	XREBOUNDS NUMBER(5,3),
	XFREEZE NUMBER(5,3),
	XPLAYSTOPPED NUMBER(5,3),
	XPLAYCONTINUEDINZONE NUMBER(5,3),
	XPLAYCONTINUEDOUTSIDEZONE NUMBER(5,3),
	FLURRYADJUSTEDXGOALS NUMBER(5,3),
	SCOREVENUEADJUSTEDXGOALS NUMBER(5,3),
	FLURRYSCOREVENUEADJUSTEDXGOALS NUMBER(5,3),
	SHOTSONGOAL NUMBER(3,0),
	MISSEDSHOTS NUMBER(3,0),
	BLOCKEDSHOTATTEMPTS NUMBER(3,0),
	SHOTATTEMPTS NUMBER(3,0),
	GOALS NUMBER(3,0),
	REBOUNDS NUMBER(3,0),
	REBOUNDGOALS NUMBER(3,0),
	FREEZE NUMBER(3,0),
	PLAYSTOPPED NUMBER(3,0),
	PLAYCONTINUEDINZONE NUMBER(3,0),
	PLAYCONTINUEDOUTSIDEZONE NUMBER(3,0),
	SAVEDSHOTSONGOAL NUMBER(3,0),
	SAVEDUNBLOCKEDSHOTATTEMPTS NUMBER(3,0),
	PENALTIES NUMBER(3,0),
	PENALITYMINUTES NUMBER(3,0),
	FACEOFFSWON NUMBER(3,0),
	HITS NUMBER(3,0),
	TAKEAWAYS NUMBER(3,0),
	GIVEAWAYS NUMBER(3,0),
	LOWDANGERSHOTS NUMBER(3,0),
	MEDIUMDANGERSHOTS NUMBER(3,0),
	HIGHDANGERSHOTS NUMBER(3,0),
	LOWDANGERXGOALS NUMBER(5,3),
	MEDIUMDANGERXGOALS NUMBER(5,3),
	HIGHDANGERXGOALS NUMBER(5,3),
	LOWDANGERGOALS NUMBER(3,0),
	MEDIUMDANGERGOALS NUMBER(3,0),
	HIGHDANGERGOALS NUMBER(3,0),
	SCOREADJUSTEDSHOTSATTEMPTS NUMBER(5,3),
	UNBLOCKEDSHOTATTEMPTS NUMBER(3,0),
	SCOREADJUSTEDUNBLOCKEDSHOTATTEMPTS NUMBER(5,3),
	DZONEGIVEAWAYS NUMBER(3,0),
	XGOALSFROMXREBOUNDSOFSHOTS NUMBER(5,3),
	XGOALSFROMACTUALREBOUNDSOFSHOTS NUMBER(5,3),
	REBOUNDXGOALS NUMBER(5,3),
	TOTALSHOTCREDIT NUMBER(5,3),
	SCOREADJUSTEDTOTALSHOTCREDIT NUMBER(5,3),
	SCOREFLURRYADJUSTEDTOTALSHOTCREDIT NUMBER(5,3),
	primary key (ID)
);