from dataclasses import dataclass, asdict
from typing import Union
from nltk.sentiment import SentimentIntensityAnalyzer
from code.spotify import Spotify


@dataclass(unsafe_hash=True)
class BaseSong:

    artist: str = None
    track: str = None
    description: str = None
    _sp = None
    _sia = SentimentIntensityAnalyzer()

    def get_duration(self):
        return self._sp.get_duration()

    def get_populartiy(self):
        return self._sp.get_popularity()

    def get_genres(self):
        return self._sp.get_genres()

    def set_spotify(self):
        self._sp = Spotify(artist=self.artist, track=self.track)

    def to_dict(self):
        return asdict(self)

    def get_sentiment(self):
        return self._sia.polarity_scores(self.description)


@dataclass
class OldSong(BaseSong):
    ranking: int = None
    writers: str = None
    producer: str = None
    released: str = None
    charts: str = None
    album: str = None
    genres: str = None
    popularity: str = None
    duration: str = None
    sentiment: dict = None
    year: int = None
    records_company: str = None

    def __init__(self):
        super(OldSong).__init__()

    def get_records_company_from_released(self) -> Union[int, None]:
        try:
            year, records_company = self.released.split(', ')
            return records_company

        except ValueError:
            pass

    def get_year_from_released(self) -> Union[int, None]:
        try:
            year, records_company = self.released.split(', ')
            if year[-2] == '0':
                return int('20' + year[-2:])
            elif year[-2].isdigit():
                return int('19' + year[-2:])

        except ValueError:
            pass


@dataclass
class NewSong(BaseSong):
    ranking: int = None
    year: int = None
    writers: str = None
    genres: str = None
    popularity: str = None
    duration: str = None
    sentiment: dict = None

    def __init__(self):
        super(NewSong).__init__()
