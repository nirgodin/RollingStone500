from dataclasses import dataclass, asdict
from nltk.sentiment import SentimentIntensityAnalyzer
from typing import List
from spotify import Spotify


@dataclass(unsafe_hash=True)
class OldSong:
    ranking: int = None
    artist: str = None
    track: str = None
    writers: str = None
    producer: str = None
    released: str = None
    charts: str = None
    description: str = None
    album: str = None
    genre: str = None
    popularity: str = None
    duration: str = None
    sentiment: dict = None

    def __init__(self):
        self._sp = None
        self._sia = SentimentIntensityAnalyzer()

    def get_duration(self):
        return self._sp.get_duration()

    def get_populartiy(self):
        return self._sp.get_popularity()

    def get_genre(self):
        return self._sp.get_genres()

    def set_spotify(self):
        self._sp = Spotify(artist=self.artist, track=self.track)

    def to_dict(self):
        return asdict(self)

    def get_sentiment(self):
        return self._sia.polarity_scores(self.description)


@dataclass
class OldSongs:
    songs: List[OldSong] = None

    def get_songs(self, text: List[str]):
        self.songs = [self._get_single_song(text, index) for index in range(0, len(text), 9)]
        return self.songs

    def get_json(self):
        songs = [song.to_dict() for song in self.songs]
        rankings = list(range(len(songs), 0, -1))
        return {i: d for i, d in zip(rankings, songs)}

    def _get_single_song(self, text: List[str], starting_index: int) -> OldSong:
        song = OldSong()
        song = self._get_rolling_stone_features(song, text, starting_index)
        song = self._get_spotify_features(song)
        song = self._get_sentiment(song)

        return song

    @staticmethod
    def _get_rolling_stone_features(song: OldSong, text: List[str], starting_index: int) -> OldSong:
        song.ranking = int(text[starting_index])
        song.artist = text[starting_index + 1]
        song.track = text[starting_index + 2]
        song.writers = text[starting_index + 3]
        song.producer = text[starting_index + 4]
        song.released = text[starting_index + 5]
        song.charts = text[starting_index + 6]
        song.description = text[starting_index + 7]
        song.album = text[starting_index + 8]

        return song

    @staticmethod
    def _get_spotify_features(song: OldSong) -> OldSong:
        try:
            song.set_spotify()
            song.genre = song.get_genre()
            song.popularity = song.get_populartiy()
            song.duration = song.get_duration()
        except (IndexError, AttributeError, TypeError) as e:
            return song

        return song

    @staticmethod
    def _get_sentiment(song: OldSong) -> OldSong:
        song.sentiment = song.get_sentiment()

        return song
