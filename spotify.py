from typing import Union
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class Spotify:

    def __init__(self, artist: str, track: str):
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self._track = self._get_track(artist, track)
        self._artist = self._get_artist()

    def get_duration(self):
        try:
            return self._track['duration_ms']
        except (IndexError, AttributeError, TypeError) as e:
            return None

    def get_popularity(self) -> Union[int, None]:
        try:
            return self._track['popularity']
        except (IndexError, AttributeError, TypeError) as e:
            return None

    def get_genre(self) -> Union[str, None]:
        try:
            return self._artist["genres"][0]
        except (IndexError, AttributeError, TypeError) as e:
            return None

    def _get_artist(self):
        try:
            artist = self._track["artists"][0]["external_urls"]["spotify"]
            return self.sp.artist(artist)
        except (IndexError, AttributeError, TypeError) as e:
            return None

    def _get_track(self, artist: str, track: str):
        try:
            track_id = self._get_track_id(artist, track)
            return self.sp.track(track_id)
        except (IndexError, AttributeError, TypeError) as e:
            return None

    def _get_track_id(self, artist: str, track: str) -> Union[dict, None]:
        try:
            query_result = self.sp.search(q="artist:" + artist + " track:" + track, type="track")
            return query_result['tracks']['items'][0]['uri']
        except (IndexError, AttributeError, TypeError) as e:
            return None
