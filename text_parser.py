import re
from typing import List


class TextParser:

    def __init__(self, path: str):
        self.text: List[str] = self._read_text(path)

    def parse_text(self) -> List[str]:
        self._drop_newlines()
        self._drop_apple_music()
        self._split_song_from_artist()
        self._drop_writers()
        self._drop_backslash_from_name()

        return self.text

    def _drop_backslash_from_name(self):
        self.text = [re.sub(r'\\', '', e) for e in self.text]
        return self.text

    def _split_song_from_artist(self) -> List[str]:
        for i in range(len(self.text)):
            if self.text[i].__contains__(", '"):
                artist, song = self.text[i].split(", '")
                self.text[i] = artist
                self.text.insert(i+1, song)

        return self.text

    def _drop_apple_music(self) -> List[str]:
        self.text = [e for e in self.text if e not in {'Powered byApple Music', 'Play the Full Song'}]
        return self.text

    def _drop_writers(self) -> List[str]:
        self.text = [re.sub("WRITER\(S\):", "", line) for line in self.text]
        return self.text

    def _drop_newlines(self) -> List[str]:
        self.text = [e for e in self.text if e != '\n']
        self.text = [re.sub("\n", "", line) for line in self.text]

        return self.text

    @staticmethod
    def _read_text(path: str) -> List[str]:
        with open(path, encoding='utf8') as f:
            return f.readlines()
