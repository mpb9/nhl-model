from enum import Enum, unique


# MARK: Environments
class Env(Enum):
    DEV = "http://127.0.0.1:8000"
    PROD = "https://dump-n-chase.com"
    ACTIVE = DEV


# MARK: Interfaces
@unique
class Interface(Enum):
    API = "/api"
    GUI = "/gui"


# MARK: API Paths
@unique
class ApiEndpoint(Enum):
    DATA = Interface.API.value + "/data"
    MODELS = Interface.API.value + "/models"
    GLOSSARY = Interface.API.value + "/glossary"
    UTILS = Interface.API.value + "/utils"


# MARK: GUI Endpoints
@unique
class GuiEndpoint(Enum):
    HOME = ""
    CONTENTS = "/contents"
    GLOSSARY = "/glossary"


# MARK: GUI File Paths
@unique
class GuiFilePath(Enum):
    HOME = "pages/home.html"
    CONTENTS = "pages/contents.html"
    GLOSSARY = "pages/glossary.html"
