import re

IRRELEVANT_STRINGS = {
    '\n',
    '\\',
    'Producer: ',
    'Released: ',
    'WRITER(S):',
    'Writer:',
    'Appears on: '
}

IRRELEVANT_STRINGS_REGEX = re.compile('|'.join(IRRELEVANT_STRINGS))

IRRELEVANT_ROWS = {
    'Powered byApple Music',
    'Play the Full Song',
    'RELATED:',
    '\n'
}
