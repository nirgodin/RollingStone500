import re
from typing import List
from code.consts import IRRELEVANT_ROWS, IRRELEVANT_STRINGS_REGEX


class TextParser:

    def __init__(self, path: str):
        self.text: List[str] = self._read_text(path)

    def parse_old_text(self) -> List[str]:
        self._drop_irrelevant_rows()
        self._split_song_from_artist()
        self._drop_irrelevant_strings()
        self._drop_backslash_from_name()
        self._organize_list()

        return self.text

    def parse_new_text(self) -> List[str]:
        self._drop_irrelevant_rows()
        self._split_song_from_artist()
        self._drop_irrelevant_strings()
        self._drop_backslash_from_name()

        return self.text

    def _organize_list(self):
        i = 0
        while i <= len(self.text) - 1:
            if self.text[i].isdigit():
                i += 9
            else:
                self.text[i-2] += self.text[i-1]
                self.text.pop(i-1)
                i = 0
                return self._organize_list()

    def _drop_backslash_from_name(self):
        self.text = [e.replace('\\', '') for e in self.text]
        return self.text

    def _split_song_from_artist(self) -> List[str]:
        formatted_text = []
        for index, value in enumerate(self.text):
            if value.__contains__(", '"):
                artist, song = value.split(", '")[:2]
                formatted_text.append(artist)
                formatted_text.append(song)
            else:
                formatted_text.append(value)

        self.text = formatted_text
        return self.text

    def _drop_irrelevant_rows(self) -> List[str]:
        self.text = [e for e in self.text
                     if e not in IRRELEVANT_ROWS and not e.__contains__('•')]
        return self.text

    def _drop_irrelevant_strings(self) -> List[str]:
        self.text = [re.sub(IRRELEVANT_STRINGS_REGEX, "", line) for line in self.text]
        return self.text

    @staticmethod
    def _read_text(path: str) -> List[str]:
        with open(path, encoding='utf8') as f:
            return f.readlines()
