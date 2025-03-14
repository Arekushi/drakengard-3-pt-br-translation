import contextlib
import typer
from rich.console import Console

from config import settings, ROOT_DIR
from src.helpers.path_helper import copy_file, has_folder, delete
from src.miscellaneous.install_maker import delete_mark
from src.miscellaneous.rpcs3_path import ensure_sqe3x0game_path


console = Console()
app = typer.Typer(help=settings.TYPER.UNINSTALL.help)


XXX_FILES = settings.FILES.xxx_files
BACKUP_FOLDER_NAME = settings.FOLDERS.backup_folder_name
SOURCE_FOLDER_NAME = settings.FOLDERS.source_folder_name


@app.command('uninstall', help=settings.TYPER.UNINSTALL.help)
def uninstall_command():
    console.rule(settings.CLI.UNINSTALL.rule)
    ensure_sqe3x0game_path()
    
    try:
        with console.status(settings.CLI.UNINSTALL.status, spinner='moon'):
            uninstall()
            console.print(settings.CLI.UNINSTALL.finish)
    except Exception:
        console.print(settings.CLI.UNINSTALL.failed)
        console.print_exception(show_locals=True)


def uninstall():
    sqex_path = settings.PATHS.SQEX03GAME_path
    backup_path = f'{sqex_path}\\{BACKUP_FOLDER_NAME}'
    source_files = [f'{ROOT_DIR}\\{SOURCE_FOLDER_NAME}\\{file}' for file in XXX_FILES]
    
    if has_folder(backup_path):
        source_files = [f'{sqex_path}\\{BACKUP_FOLDER_NAME}\\{file}' for file in XXX_FILES]
    
    for file in source_files:
        copy_file(file, sqex_path)
    
    with contextlib.suppress(FileNotFoundError, OSError, ValueError):
        delete(backup_path)
    
    with contextlib.suppress(FileNotFoundError, OSError, ValueError):
        delete_mark(sqex_path)
