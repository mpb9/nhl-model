import pandas as pd

from src.utility.personal import tidy_up, drop_nulls
from utility.constants import DB_PATH


class CsvExport(object):
    """Export a dataframe to a csv file

    Args:
        df (pd.Dataframe): dataframe to be exported
        szn (str, optional): season(s) included in dataframe. Defaults to ''.
        sit (str, optional): situation specific to dataframe. Defaults to '5on5'.
        subfol (str, optional): subfolder to save csv file in. Defaults to ''.
        name (str, optional): custom string appended to end of csv file's name. Defaults to ''.
        no_nulls (bool, optional): whether to drop null values before exporting. Defaults to True.
        tidy (bool, optional): whether to tidy up the dataframe before exporting. Defaults to True.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        szn="",
        sit="5on5",
        subfol="",
        name="",
        tidy=True,
        no_nulls=True,
    ):
        self.df = df
        self.file_path = self.path_builder(szn, sit, name, subfol)

    def path_builder(self, szn, sit, name, subfol):
        return (
            DB_PATH
            + f"{szn}{'' if not bool(subfol) else f'/{subfol}'}/{'' if not bool(name) else f'{name}_'}{sit}{'' if not bool(szn) else f'_{szn}'}.csv"
        )
