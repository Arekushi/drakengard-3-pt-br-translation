import json
from config import settings
from datetime import datetime
from src.helpers.path_helper import has_file, delete


TRANSLATION_FILE_NAME = settings.FILEs.translation_json_file


def mark_translation_installed(
    game_path: str,
    commit_sha: str,
    release_version: str
):
    data = {
        'release_version': release_version,
        'commit_sha': commit_sha,
        'install_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    file_path = f'{game_path}\\{TRANSLATION_FILE_NAME}'
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
        

def delete_mark(game_path: str):
    delete(f'{game_path}\\{TRANSLATION_FILE_NAME}')


def is_translation_installed(game_path: str) -> bool:
    return has_file(f'{game_path}\\{TRANSLATION_FILE_NAME}')
