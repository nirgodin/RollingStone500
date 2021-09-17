import json
import re
from collections import Counter
from typing import Generator, List
import pandas as pd
from pandas import DataFrame


class PreProcessor:

    def __init__(self, rolling_stone_path: str, artists_info_path: str):
        self.data = self._to_dataframe(self._read_data(rolling_stone_path))
        self.artists_info = pd.read_csv(artists_info_path)

    def add_single_genre(self):
        self.data['single_genre'] = self.data['genre'].apply(lambda g: self._get_main_genre(g))
        self.data['single_genre'] = [re.sub('hip', 'hip hop', g) for g in self.data['single_genre']]
        return self.data

    def _add_artists_info(self):
        self.data = self.data.merge(right=self.artists_info,
                                    how='left',
                                    on='artist')

    @staticmethod
    def _get_main_genre(genres: List[str]):
        if genres and genres != []:
            genre_concat = ' '.join(genres)
            genre_tokens = genre_concat.split(' ')
            return Counter(genre_tokens).most_common(1)[0][0]

        return ''

    def _to_dataframe(self, json_data: dict) -> DataFrame:
        return pd.concat(list(self._map_data_to_dataframes(json_data)))

    def _map_data_to_dataframes(self, json_data: dict) -> Generator[DataFrame, None, None]:
        return (self._dict_to_df(d) for d in json_data.values())

    @staticmethod
    def _dict_to_df(d: dict) -> DataFrame:
        return pd.DataFrame.from_dict(data=d, orient='index').transpose()

    @staticmethod
    def _read_data(path: str) -> dict:
        with open(path, encoding='utf8') as f:
            return json.loads(f.read())

#
# processor = PreProcessor('new_data.txt', 'list_of_artists.csv')
# processor.add_artists_info()
# processor.add_single_genre()
# data = processor.df_data
# genres_dict = {'grunge': 'rock',
#                'rap': 'hip hop',
#                'punk': 'rock',
#                'rock-and-roll': 'rock',
#                'beatlesque': 'rock',
#                'europop': 'pop',
#                'electropop': 'pop',
#                'synthpop': 'pop',
#                'k-pop': 'pop',
#                'mexican': 'world',
#                'cha-cha-cha': 'world',
#                'bossa': 'world',
#                'latin': 'world',
#                'house': 'electro'}
# data['single_genre'] = [genres_dict[g] if g in genres_dict.keys() else g
#                         for g in data['single_genre']]
# # a = pd.DataFrame(data['single_genre'].unique())[0].tolist()
# data.to_csv(r'new_df_data.csv', index=False)
