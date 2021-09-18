import json
from songs import Songs
from text_parser import TextParser

OLD_PATH = 'resources/raw/old_list.txt'
NEW_PATH = 'resources/raw/rolling_stone_text.txt'


# # Create old songs objects and modify to json
# old_text = TextParser(OLD_PATH).parse_old_text()
# old_songs = Songs(song_type='old')
# old_rs = old_songs.get_songs(old_text)
# old_data = old_songs.get_json()
#
# # Export data
# with open('resources/processed/old_data.txt', 'w', encoding='utf8') as outfile:
#     json.dump(old_data, outfile, indent=4, sort_keys=True)

# Create new songs objects and modify to json
new_text = TextParser(NEW_PATH).parse_new_text()
new_songs = Songs(song_type='new')
new_rs = new_songs.get_songs(new_text)
new_data = new_songs.get_json()

# Export data
with open('resources/processed/new_data.txt', 'w', encoding='utf8') as outfile:
    json.dump(new_data, outfile, indent=4, sort_keys=True)
