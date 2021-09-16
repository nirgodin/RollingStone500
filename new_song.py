from dataclasses import dataclass, asdict
from nltk.sentiment import SentimentIntensityAnalyzer
from typing import List
from spotify import Spotify


@dataclass(unsafe_hash=True)
class NewSong:
    ranking: int = None
    artist: str = None
    track: str = None
    year: int = None
    writers: str = None
    description: str = None
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
        return self._sp.get_genre()

    def set_spotify(self):
        self._sp = Spotify(artist=self.artist, track=self.track)

    def to_dict(self):
        return asdict(self)

    def get_sentiment(self):
        return self._sia.polarity_scores(self.description)


@dataclass
class NewSongs:
    songs: List[NewSong] = None

    def get_songs(self, text: List[str]):
        self.songs = [self._get_single_song(text, index) for index in range(0, len(text), 6)]
        return self.songs

    def get_json(self):
        songs = [song.to_dict() for song in self.songs]
        rankings = list(range(len(songs), 0, -1))
        return {i: d for i, d in zip(rankings, songs)}

    def _get_single_song(self, text: List[str], starting_index: int) -> NewSong:
        song = NewSong()
        song = self._get_rolling_stone_features(song, text, starting_index)
        song = self._get_spotify_features(song)
        song = self._get_sentiment(song)

        return song

    @staticmethod
    def _get_rolling_stone_features(song: NewSong, text: List[str], starting_index: int) -> NewSong:
        song.ranking = int(text[starting_index])
        song.artist = text[starting_index+1]
        song.track = text[starting_index + 2]
        song.year = int(text[starting_index+3])
        song.writers = text[starting_index+4]
        song.description = text[starting_index+5]

        return song

    @staticmethod
    def _get_spotify_features(song: NewSong) -> NewSong:
        song.set_spotify()
        song.genre = song.get_genre()
        song.popularity = song.get_populartiy()
        song.duration = song.get_duration()

        return song

    @staticmethod
    def _get_sentiment(song: NewSong) -> NewSong:
        song.sentiment = song.get_sentiment()

        return song
