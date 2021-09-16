from dataclasses import dataclass, asdict
from typing import List
from spotify import Spotify


@dataclass(unsafe_hash=True)
class Song:
    ranking: int = None
    artist: str = None
    track: str = None
    year: int = None
    writers: str = None
    description: str = None
    genre: str = None
    popularity: str = None
    duration: str = None

    def __init__(self):
        self.sp = None

    def get_duration(self):
        return self.sp.get_duration()

    def get_populartiy(self):
        return self.sp.get_popularity()

    def get_genre(self):
        return self.sp.get_genre()

    def set_spotify(self):
        self.sp = Spotify(artist=self.artist, track=self.track)

    def to_dict(self):
        return asdict(self)


@dataclass
class Songs:
    songs: List[Song] = None

    def get_songs(self, text: List[str]):
        self.songs = [self._get_single_song(text, index) for index in range(0, len(text), 6)]
        return self.songs

    def get_json(self):
        songs = [song.to_dict() for song in self.songs]
        rankings = list(range(len(songs), 0, -1))
        return {i: d for i, d in zip(rankings, songs)}

    @staticmethod
    def _get_single_song(text: List[str], starting_index: int) -> Song:
        song = Song()
        song.ranking = int(text[starting_index])
        song.artist = text[starting_index+1]
        song.track = text[starting_index + 2]
        song.year = int(text[starting_index+3])
        song.writers = text[starting_index+4]
        song.description = text[starting_index+5]
        song.set_spotify()
        song.genre = song.get_genre()
        song.popularity = song.get_populartiy()
        song.duration = song.get_duration()

        return song
