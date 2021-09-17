from typing import Union, List
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


DURATION = 'duration_ms'
POPULARITY = 'popularity'
GENRES = 'genres'
ARTISTS = 'artists'
EXTERNAL_URLS = 'external_urls'
SPOTIFY = 'spotify'
TRACKS = 'tracks'
ITEMS = 'items'
URI = 'uri'


class Spotify:

    def __init__(self, artist: str, track: str):
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self._track = self._get_track(artist, track)
        self._artist = self._get_artist()

    def get_duration(self):
        return self._track[DURATION]

    def get_popularity(self) -> Union[int, None]:
        return self._track[POPULARITY]

    def get_genres(self) -> Union[List[str], None]:
        return self._artist[GENRES]

    def _get_artist(self):
        artist = self._track[ARTISTS][0][EXTERNAL_URLS][SPOTIFY]
        return self.sp.artist(artist)

    def _get_track(self, artist: str, track: str):
        track_id = self._get_track_id(artist, track)
        return self.sp.track(track_id)

    def _get_track_id(self, artist: str, track: str) -> Union[dict, None]:
        query_result = self.sp.search(q="artist:" + artist + " track:" + track, type="track")
        return query_result[TRACKS][ITEMS][0][URI]
