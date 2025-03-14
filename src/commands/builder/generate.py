import os
import typer
import json
import subprocess
from typing import List
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.helpers.path_helper import has_folder, make_dir
from src.helpers.zip_helper import unzip_file
from src.helpers.pandas_helper import concatenate_csv_files, save_df_txt, get_all_files

TEXTS_PATH = f'{ROOT_DIR}\\texts'
PATCH_PATH = f'{ROOT_DIR}\\{settings.FOLDERS.patch_folder_name}'
TOOLS_PATH = f'{ROOT_DIR}\\{settings.FOLDERS.tools_folder_name}'
RESULT_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.result_folder_name}'
EXPORT_FILE_PATH = f'{RESULT_PATH}\\{settings.FILES.export_json_file}'
TRANSLATION_FOLDER_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.translation_folder_name}'

SQEX_ZIP = f'{TOOLS_PATH}\\{settings.FILES.sqex_zip_file}'
SQEX_PATH = SQEX_ZIP[0:-4]
SQEX_EXE = f'{SQEX_PATH}\\{settings.FILES.sqex_exe_file}'

console = Console()
app = typer.Typer(
    help=settings.TYPER.GENERATE.help
)


@app.command(
    'generate',
    help=settings.TYPER.GENERATE.help
)
def generate_command():
    console.rule(settings.CLI.GENERATE.rule)
    
    try:
        with console.status(settings.CLI.GENERATE.status, spinner='moon'):
            if not has_folder(SQEX_PATH):
                unzip_file(SQEX_ZIP, SQEX_PATH)
            
            create_result_files()
            generate_xxx_files()
        
        console.print(settings.CLI.GENERATE.finish)
    except (Exception) as e:
        console.print(e)
        console.print(settings.CLI.GENERATE.failed)


def generate_xxx_files():
    subprocess.run(
        f'{SQEX_EXE} repack -s {PATCH_PATH} -p {RESULT_PATH} -o'
    )


def create_result_files():
    make_dir(RESULT_PATH)
    
    translated_files = get_all_translation_files()
    ordered_files = order_translated_files(translated_files)
    df = concatenate_csv_files(ordered_files)
    save_df_txt(df['translation'], f'{RESULT_PATH}\\{settings.FILES.result_file_name}')


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
