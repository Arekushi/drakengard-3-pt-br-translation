import typer
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.helpers.pandas_helper import read_raw_file, transform_raw_df, save_df
from src.helpers.path_helper import get_all_files, make_dir, update_dir


texts_path = f'{ROOT_DIR}\\texts'
raw_texts_files_path = f'{texts_path}\\{settings.FOLDERS.raw_texts_folder_name}'
translation_folder_path = f'{texts_path}\\{settings.FOLDERS.translation_folder_name}'

console = Console()
app = typer.Typer(
    help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help,
    callback=lambda: make_dir(translation_folder_path)
)

@app.command(
    'make-translation-folder',
    help=settings.TYPER.MAKE_TRANSLATION_FOLDER.help,
)
def make_translation_folder_command():
    console.rule(settings.CLI.MAKE_TRANSLATION_FOLDER.rule)
    
    with console.status(
        settings.CLI.MAKE_TRANSLATION_FOLDER.status,
        spinner='moon'
    ):
        create_translation_folder()


def create_translation_folder():
    raw_files = get_all_files(raw_texts_files_path)
    
    for file in raw_files:
        df = read_raw_file(file)
        df = transform_raw_df(df)
        new_file_path = update_dir(file, translation_folder_path)
        save_df(df, new_file_path)
