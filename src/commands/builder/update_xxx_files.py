import typer
import pandas as pd
from rich.console import Console

from config.config import settings, ROOT_DIR
from src.helpers.path_helper import remove_file
from src.helpers.string_helper import remove_brackets
from src.helpers.pandas_helper import concatenate_csv_files, save_df_csv
from src.helpers.hex_helper import replace_hex, convert_str_to_hex


TEXTS_PATH = f'{ROOT_DIR}\\texts'
TRANSLATION_FOLDER_PATH = f'{TEXTS_PATH}\\{settings.FOLDERS.translation_folder_name}'
PATCH_FOLDER_PATH = f'{ROOT_DIR}\\{settings.FOLDERS.patch_folder_name}'
SOURCE_FOLDER_PATH = f'{ROOT_DIR}\\{settings.FOLDERS.source_folder_name}'
TEMP_FOLDER_PATH = f'{ROOT_DIR}\\{settings.FOLDERS.temp_folder_name}'
LOG_FILE_PATH = f'{TEMP_FOLDER_PATH}\\{settings.FILES.update_xxx_log}'


console = Console()
app = typer.Typer(
    help=settings.TYPER.UPDATE_XXX.help
)


def remove_xxx_files():    
    for file in settings.FILES.to_edit_hex:
        remove_file(f'{PATCH_FOLDER_PATH}\\{file}')


@app.command(
    'update-xxx',
    help=settings.TYPER.UPDATE_XXX.help
)
def update_xxx_command():
    console.rule(settings.CLI.UPDATE_XXX.rule)
    remove_xxx_files()
    
    with console.status(
        settings.CLI.UPDATE_XXX.status,
        spinner='moon'
    ):
        update_xxx_files()


def update_xxx_files():
    df = concatenate_csv_files(TRANSLATION_FOLDER_PATH)
    df = df.query("can_modify == '0'")
    df = df.applymap(remove_brackets)
    translations_needing_padding = []
    
    for transalation, source in zip(df['translation'].to_list(), df['source'].to_list()):
        try:
            translation_hex = convert_str_to_hex(transalation, encoding='latin-1')
            source_hex = convert_str_to_hex(source, encoding='latin-1')
            len_diff = len(source_hex) - len(translation_hex)
            
            if (len_diff < 0):
                translations_needing_padding.append({
                    'translation': transalation,
                    'source': source
                })
                continue
            elif (len_diff > 0):
                translation_hex = translation_hex.ljust(len(source_hex), '0')
            
            for file_name in settings.FILES.to_edit_hex:
                file_path = f'{SOURCE_FOLDER_PATH}\\{file_name}'
                dest_file_path = f'{PATCH_FOLDER_PATH}\\{file_name}'
                replace_hex(file_path, source_hex, translation_hex, dest_file_path)
        except (UnicodeDecodeError, UnicodeEncodeError):
            continue
    
    if (translations_needing_padding):
        translations_needing_padding = pd.concat(
            [pd.DataFrame(translations_needing_padding)],
            ignore_index=True
        )
        
        save_df_csv(
            translations_needing_padding,
            LOG_FILE_PATH
        )
