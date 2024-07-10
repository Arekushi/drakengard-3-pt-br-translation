import typer
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.helpers.pandas_helper import read_raw_file, transform_raw_df, save_df_csv
from src.helpers.path_helper import get_all_files, make_dir, update_dir


TEXTS_PATH = f'{ROOT_DIR}\\texts'
RAW_TEXTS_FILES_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.raw_texts_folder_name}'
TRANSLATION_FOLDER_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.translation_folder_name}'

console = Console()
app = typer.Typer(
    help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help
)

@app.command(
    'make-translation-folder',
    help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help,
)
def make_translation_folder_command():
    console.rule(settings.CLI.MAKE_TRANSLATION_FOLDER.rule)
    make_dir(TRANSLATION_FOLDER_PATH)
    
    with console.status(
        settings.CLI.MAKE_TRANSLATION_FOLDER.status,
        spinner='moon'
    ):
        create_translation_folder()


def create_translation_folder():
    raw_files = get_all_files(RAW_TEXTS_FILES_PATH)
    
    for file_path in raw_files:
        df = read_raw_file(file_path)
        df = transform_raw_df(df)
        new_file_path = update_dir(file_path, TRANSLATION_FOLDER_PATH)
        save_df_csv(df, new_file_path)
