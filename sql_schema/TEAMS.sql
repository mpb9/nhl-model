create or replace TABLE TEAMS (
	TEAM_ID NUMBER(2,0) NOT NULL,
	TEAM_NAME VARCHAR(3) NOT NULL,
	unique (TEAM_NAME),
	primary key (TEAM_ID)
);
