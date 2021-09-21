import json
import pandas as pd
from code.pre_processor import PreProcessor
from code.songs import Songs
from code.text_parser import TextParser

IMPORT_PATHS = [
    'resources/raw/2004_rolling_stone_list.txt',
    'resources/raw/2021_rolling_stone_list.txt'
]

DATA_TYPES = [
    'old',
    'new'
]

EXPORT_PATHS = [
    'resources/processed/old_data.txt',
    'resources/processed/new_data.txt'
]


if __name__ == '__main__':

    dataframes = []
    for import_path, data_type, export_path in zip(IMPORT_PATHS, DATA_TYPES, EXPORT_PATHS):

        # Parse text
        text = TextParser(import_path, data_type).parse_text()

        # Extract songs information from text
        songs = Songs(song_type=data_type)
        songs.get_songs(text)

        # Pass data to json format and export
        json_data = songs.get_json()
        with open(export_path, 'w', encoding='utf8') as outfile:
            json.dump(json_data, outfile, indent=4, sort_keys=True)

        # Pre process json data to pandas dataframe
        pandas_data = PreProcessor(export_path, data_type).pre_process()
        dataframes.append(pandas_data)

    # Concatenate two data objects results to one final dataframe and export
    data = pd.concat(dataframes,
                     join='outer').drop_duplicates(subset=['ranking', 'data_type'])
    data.to_csv(r'data.csv', index=False)
