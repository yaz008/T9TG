from os import listdir, getenv
from json import load

MATCH: str = getenv(key='MATCH')

def _load_file(path: str) -> dict[str, str]:
    with open(file=path, mode='r', encoding='UTF-8') as match_file:
        return load(match_file)

def load_all() -> dict[str, str]:
    matches: dict[str, str] = dict()
    for match_file in listdir(MATCH):
        matches.update(_load_file(f'{MATCH}\\{match_file}'))
    return matches