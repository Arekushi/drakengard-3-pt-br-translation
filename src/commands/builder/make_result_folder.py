import os
import typer
import json
from typing import List
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.helpers.pandas_helper import concatenate_csv_files, save_df_txt, get_all_files
from src.helpers.path_helper import make_dir


TEXTS_PATH = f'{ROOT_DIR}\\texts'
TRANSLATION_FOLDER_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.translation_folder_name}'
RESULT_FOLDER_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.result_folder_name}'
EXPORT_FILE_PATH = f'{RESULT_FOLDER_PATH}\\{settings.FILES.export_json_file}'

console = Console()
app = typer.Typer(
    help=settings.TYPER.MAKE_RESULT_FOLDER.help
)

@app.command(
    'make-result-folder',
    help=settings.TYPER.MAKE_RESULT_FOLDER.help,
)
def make_result_folder_command():
    console.rule(settings.CLI.MAKE_RESULT_FOLDER.rule)
    make_dir(RESULT_FOLDER_PATH)
    
    with console.status(
        settings.CLI.MAKE_RESULT_FOLDER.status,
        spinner='moon'
    ):
        create_result_folder()


def create_result_folder():
    translated_files = get_all_translation_files()
    ordered_files = order_translated_files(translated_files)
    df = concatenate_csv_files(ordered_files)
    save_df_txt(df['translation'], f'{RESULT_FOLDER_PATH}\\{settings.FILES.result_file_name}')


def order_translated_files(translated_files: List[str]):
    with open(f'{EXPORT_FILE_PATH}', 'r', encoding='utf-8') as file:
        order_dict = json.load(file)
        ordered_keys = [key.lower() for key in order_dict.keys()]
        sorted_files = sorted(
            translated_files,
            key=lambda x: ordered_keys.index(os.path.splitext(os.path.basename(x))[0].lower())
        )
        return sorted_files


def get_all_translation_files():
    files = get_all_files(TRANSLATION_FOLDER_PATH)
    return [file for file in files if file.lower().endswith('.csv')]
