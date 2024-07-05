from enum import Enum, unique
from api_config.utils.paths.env_path_config import Env


# MARK: API PATH
@unique
class ApiPath(Enum):
    PREFIX = "/api"
    DATA = Env.ACTIVE.value + PREFIX + "/data"
    MODELS = Env.ACTIVE.value + PREFIX + "/models"
    GLOSSARY = Env.ACTIVE.value + PREFIX + "/glossary"
    UTILS = Env.ACTIVE.value + PREFIX + "/utils"


# MARK: NHL Game Data
@unique
class Data(Enum):
    TEMP = ""


# MARK: NHL Models
@unique
class Models(Enum):
    TEMP = ""


# MARK: Glossary
@unique
class Glossary(Enum):
    GET_SEASONS = ApiPath.GLOSSARY.value + "/seasons"
    GET_TEAMS = ApiPath.GLOSSARY.value + "/teams"


# MARK: Utils
@unique
class Utils(Enum):
    TEMP = ""
