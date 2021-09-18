from dataclasses import dataclass
from typing import List, Union, Dict
from spotipy import SpotifyException
from song import OldSong, NewSong


@dataclass
class Songs:
    songs: List[Union[OldSong, NewSong]] = None

    def __init__(self, song_type: str):
        assert song_type in ['old', 'new'], 'song type must be one of the following kinds: ["old", "new"]'
        self.song_type = song_type

    def get_json(self) -> Dict[str, dict]:
        songs = [song.to_dict() for song in self.songs]
        rankings = list(range(len(songs), 0, -1))
        return {i: d for i, d in zip(rankings, songs)}

    def get_songs(self, text: List[str]) -> List[Union[OldSong, NewSong]]:
        if self.song_type == 'old':
            self.songs = [self._get_single_song(text, index) for index in range(0, len(text), 9)]
        else:
            self.songs = [self._get_single_song(text, index) for index in range(0, len(text), 6)]
        return self.songs

    def _get_single_song(self, text: List[str], starting_index: int) -> Union[OldSong, NewSong]:
        song = self._get_song_instance(text, starting_index)
        song = self._get_spotify_features(song)
        song = self._get_sentiment(song)

        return song

    def _get_song_instance(self, text: List[str], starting_index: int) -> Union[OldSong, NewSong]:
        if self.song_type == 'old':
            song = OldSong()
            return self._get_old_rolling_stone_features(song, text, starting_index)
        else:
            song = NewSong()
            return self._get_new_rolling_stone_features(song, text, starting_index)

    @staticmethod
    def _get_old_rolling_stone_features(song: OldSong, text: List[str], starting_index: int) -> OldSong:
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
    def _get_new_rolling_stone_features(song: NewSong, text: List[str], starting_index: int) -> NewSong:
        song.ranking = int(text[starting_index])
        song.artist = text[starting_index+1]
        song.track = text[starting_index + 2]
        song.year = int(text[starting_index+3])
        song.writers = text[starting_index+4]
        song.description = text[starting_index+5]

        return song

    @staticmethod
    def _get_spotify_features(song: Union[OldSong, NewSong]) -> Union[OldSong, NewSong]:
        try:
            song.set_spotify()
            song.genre = song.get_genres()
            song.popularity = song.get_populartiy()
            song.duration = song.get_duration()
        except (IndexError, AttributeError, TypeError, SpotifyException) as e:
            return song

        return song

    @staticmethod
    def _get_sentiment(song: Union[OldSong, NewSong]) -> Union[OldSong, NewSong]:
        song.sentiment = song.get_sentiment()

        return song
