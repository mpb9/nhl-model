from enum import Enum, unique


@unique
class QueryDataBy(Enum):
    PREFIX = "/by_"
    TEAM = PREFIX + "team"
    OPPONENT = PREFIX + "opp"
    SEASON = PREFIX + "season"
    GAME = PREFIX + "game"
    SITUATION = PREFIX + "sit"


@unique
class GameSits(Enum):
    EVEN = "/5on5"
    PP = "/5on4"
    PK = "/4on5"
