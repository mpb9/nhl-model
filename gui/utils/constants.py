from enum import Enum, unique


# MARK: Environments
class Env(Enum):
    DEV = "http://127.0.0.1:8000"
    PROD = "https://dump-n-chase.com"
    ACTIVE = DEV
