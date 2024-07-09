import typer
import pandas as pd
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.helpers.pandas_helper import read_csv_file, save_df_txt
from src.helpers.path_helper import get_all_files, make_dir, update_dir


TEXTS_PATH = f'{ROOT_DIR}\\texts'
TRANSLATION_FOLDER_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.translation_folder_name}'
RESULT_FOLDER_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.result_folder_name}'

console = Console()
app = typer.Typer(
    help=settings.TYPER.MAKE_RESULT_FOLDER.help,
    callback=lambda: make_dir(RESULT_FOLDER_PATH)
)

@app.command(
    'make-result-folder',
    help=settings.TYPER.MAKE_RESULT_FOLDER.help,
)
def make_result_folder_command():
    console.rule(settings.CLI.MAKE_RESULT_FOLDER.rule)
    
    with console.status(
        settings.CLI.MAKE_RESULT_FOLDER.status,
        spinner='moon'
    ):
        create_result_folder()


def create_result_folder():
    translation_files = get_all_files(TRANSLATION_FOLDER_PATH)
    result_df = pd.DataFrame()
    
    for file_path in translation_files:
        df = read_csv_file(file_path)
        result_df = pd.concat([result_df, df['translation']])
    
    result_df = result_df.rename(columns={0: 'translation'})
    save_df_txt(result_df['translation'], f'{RESULT_FOLDER_PATH}\\{settings.FILES.result_file_name}')
