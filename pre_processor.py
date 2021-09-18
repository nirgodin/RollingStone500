import json
import re
from collections import Counter
from typing import Generator, List
import pandas as pd
from pandas import DataFrame


main_genres = [
    'rock',
    'pop',
    'hip',
    'soul',
    'blues',
    'funk',
    'jazz',
    'reggae',
    'folk',
    'singer-songwriter'
]

genres_dict = {
    'punk': 'rock',
    'rock-and-roll': 'rock',
    'k-pop': 'pop',
    'rap': 'hip',
    'r&b': 'soul',
    'mexican': 'world',
    'cha-cha-cha': 'world',
    'bossa': 'world',
    'latin': 'world',
    'country': 'folk'
}


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

    def _get_main_genre(self, genres: List[str]):
        for genre in self.yield_genre(genres):
            if genre in main_genres:
                return genre
            elif genre in genres_dict:
                return genres_dict[genre]
            else:
                pass

        return 'other'

    @staticmethod
    def yield_genre(genres: List[str]):
        if genres and genres != []:
            genre_concat = ' '.join(genres)
            genre_tokens = genre_concat.split(' ')
            return (genre[0] for genre in Counter(genre_tokens).most_common())

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


processor = PreProcessor('resources/processed/new_data.txt', 'resources/processed/list_of_artists.csv')
processor._add_artists_info()
processor.add_single_genre()
data = processor.data
da = data[data['single_genre'] == 'other']
data.to_csv(r'resources/processed/new_df_data.csv', index=False)
