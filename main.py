import json

from song import Songs
from text_parser import TextParser

PATH = 'rolling_stone_text.txt'

# Import and parse raw text
text = TextParser(PATH).parse_text()

# Create songs objects and modify to json
songs = Songs()
rs = songs.get_songs(text)
data = songs.get_json()

# Export data
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True)
