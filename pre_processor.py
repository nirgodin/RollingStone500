import json
from typing import Generator, List
import seaborn as sns
import pandas as pd
from pandas import DataFrame


class PreProcessor:

    def __init__(self, rolling_stone_path: str, artists_info_path: str):
        self.json_data = self.read_data(rolling_stone_path)
        self.df_data = self._to_dataframe()
        self.artists_info = pd.read_csv(artists_info_path)

    def _add_artists_info(self):
        pass

    def get_artists(self) -> List[str]:
        return pd.DataFrame(self.df_data['artist']).unique().tolist()

    def _to_dataframe(self) -> DataFrame:
        return pd.concat(list(self._map_data_to_dataframes()))

    def _map_data_to_dataframes(self) -> Generator[DataFrame, None, None]:
        return (self._dict_to_df(d) for d in self.json_data.values())

    @staticmethod
    def _dict_to_df(d: dict) -> DataFrame:
        return pd.DataFrame.from_dict(data=d, orient='index').transpose()

    @staticmethod
    def read_data(path: str) -> dict:
        with open(path, encoding='utf8') as f:
            return json.loads(f.read())


processor = PreProcessor('new_data.txt')
data = processor.df_data
