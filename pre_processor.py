import json
import re
from collections import Counter
from difflib import SequenceMatcher
from typing import Generator, List, Dict, Tuple
import pandas as pd
from pandas import DataFrame

ARTISTS_INFO_PATH = 'resources/raw/artists_info.csv'

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

    def __init__(self, json_data_path: str, data_type: str):
        self.data = self._to_dataframe(self._read_json_data(json_data_path))
        self.data_type = data_type

    def pre_process(self):
        self._add_artists_info()
        self._add_main_genre()
        self._add_data_type()

        return self.data

    def _add_data_type(self):
        self.data['data_type'] = self.data_type

    def _add_main_genre(self):
        self.data['main_genre'] = self.data['genres'].apply(lambda g: self._get_main_genre(g))
        self.data['main_genre'] = [re.sub('hip', 'hip hop', g) for g in self.data['main_genre']]
        return self.data

    def _add_artists_info(self):
        artists_info = pd.read_csv(ARTISTS_INFO_PATH)
        self.data = self.data.merge(right=artists_info,
                                    how='left',
                                    on='artist')

    def _get_main_genre(self, genres: List[str]):
        for genre in self._yield_most_common_genre(genres):
            if genre in main_genres:
                return genre
            elif genre in genres_dict:
                return genres_dict[genre]
            else:
                pass

        return 'other'

    def get_artists_number_of_songs(self, artists: List[str]) -> Dict[str, int]:
        counter = {}
        for new_artist in artists:
            does_artist_exist, counted_artist = self._does_artist_exist(new_artist, counter)
            if does_artist_exist:
                counter[counted_artist] += 1
            else:
                counter[new_artist] = 1

        return counter

    @staticmethod
    def _does_artist_exist(new_artist: str, counter: Dict[str, int]) -> Tuple[bool, str]:
        for counted_artist in counter.keys():
            if SequenceMatcher(None, new_artist, counted_artist).ratio() > 0.7:
                return True, counted_artist

        return False, ''
        
    @staticmethod
    def _yield_most_common_genre(genres: List[str]):
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
    def _read_json_data(path: str) -> dict:
        with open(path, encoding='utf8') as f:
            return json.loads(f.read())

