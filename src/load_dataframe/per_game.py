import numpy as np
import pandas as pd

from src.utility.personal import *
from src.utility.storage import *
from src.utility.constants import *


class PerGameData:
    df = pd.DataFrame()

    def __init__(self, szn, sit):
        self.df = retrieve_csv(
            szn,
            sit,
        )
