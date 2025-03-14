import requests
from typing import List
from rich.console import Console
from dynaconf.loaders.toml_loader import write

from config import settings, ROOT_DIR
from src.helpers.http_request_helper import download_file


console = Console()
COMMITS_URL = settings.GITHUB.commits_url
LAST_RELEASE_URL = settings.GITHUB.last_release_url
RAW_PATCH_URL = settings.GITHUB.raw_patch_url
TEMP_PATH = f'{ROOT_DIR}\\{settings.FOLDERS.temp_folder_name}'


def get_books_commits(all_commits):
    return list(filter(lambda commit: '📚' in commit['commit']['message'], all_commits))


def get_latest_commit_sha():
    response: list[dict] = requests.get(COMMITS_URL, allow_redirects=False).json()

    if response:
        last_commit = get_books_commits(response)[0]
        return last_commit['sha']

    return None


def download_patch_files(file_names: List[str]):
    file_paths = list()
    
    for file_name in file_names:
        temp_file = download_file(
            f'{RAW_PATCH_URL}/{file_name}',
            TEMP_PATH
        )
        file_paths.append(temp_file)
    
    return file_paths
