from dataclasses import dataclass, asdict
from nltk.sentiment import SentimentIntensityAnalyzer
from spotify import Spotify


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
    genre: str = None
    popularity: str = None
    duration: str = None
    sentiment: dict = None

    def __init__(self):
        super(OldSong).__init__()


@dataclass
class NewSong(BaseSong):
    ranking: int = None
    year: int = None
    writers: str = None
    genre: str = None
    popularity: str = None
    duration: str = None
    sentiment: dict = None

    def __init__(self):
        super(NewSong).__init__()
