import json
from new_song import NewSongs
from old_song import OldSongs
from text_parser import TextParser

# OLD_PATH = 'old_list.txt'
# NEW_PATH = 'rolling_stone_text.txt'
#
#
# # Create new songs objects and modify to json
# old_text = TextParser(OLD_PATH).parse_old_text()
# old_songs = OldSongs()
# old_rs = old_songs.get_songs(old_text)
# old_data = old_songs.get_json()
#
# # Export data
# with open('old_data.txt', 'w', encoding='utf8') as outfile:
#     json.dump(old_data, outfile, indent=4, sort_keys=True)
#
# # Create new songs objects and modify to json
# new_text = TextParser(NEW_PATH).parse_new_text()
# new_songs = NewSongs()
# new_rs = new_songs.get_songs(new_text)
# new_data = new_songs.get_json()
#
# # Export data
# with open('new_data.txt', 'w', encoding='utf8') as outfile:
#     json.dump(new_data, outfile, indent=4, sort_keys=True)


# Read data
data = TextParser().read_text('new_data.txt')
