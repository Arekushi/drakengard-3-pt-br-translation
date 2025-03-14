import typer
from rich.console import Console

from config import settings, ROOT_DIR
from src.miscellaneous.github_requests import download_patch_files, get_latest_commit_sha
from src.helpers.path_helper import copy_file
from src.miscellaneous.install_maker import is_translation_installed, mark_translation_installed
from src.miscellaneous.rpcs3_path import ensure_sqe3x0game_path


console = Console()
app = typer.Typer(help=settings.TYPER.INSTALL.help)

PATCH_FILES = settings.FILES.xxx_files
BACKUP_FOLDER_NAME = settings.FOLDERS.backup_folder_name
PATCH_FOLDER_NAME = settings.FOLDERS.patch_folder_name
CURRENT_RELEASE_VERSIOIN = settings.GITHUB.current_release_version


@app.command('install', help=settings.TYPER.INSTALL.help)
def install_command(
    is_locally: bool = typer.Option(
        False,
        '--local',
        help=settings.TYPER.INSTALL.install_locally_help
    )
):
    console.rule(settings.CLI.INSTALL.rule)
    ensure_sqe3x0game_path()
    
    try:
        with console.status(settings.CLI.INSTALL.status, spinner='moon'):
            install(is_locally)
            console.print(settings.CLI.INSTALL.finish)
            
            if not is_locally:
                console.print(settings.CLI.thanks, justify='center')
    except Exception:
        console.print(settings.CLI.INSTALL.failed)
        console.print_exception(show_locals=True)


def install(is_locally = False):
    sqex_path = settings.PATHS.SQEX03GAME_path
    to_install_files = [f'{ROOT_DIR}\\{PATCH_FOLDER_NAME}\\{file}' for file in PATCH_FILES]
    
    if not is_locally:
        if not is_translation_installed(sqex_path):
            console.print(settings.CLI.INSTALL.backup)
            backup_files(sqex_path)
        
        to_install_files = download_patch_files(PATCH_FILES)
        console.print(settings.CLI.INSTALL.download_finished)
        
        mark_translation_installed(
            sqex_path,
            get_latest_commit_sha(),
            CURRENT_RELEASE_VERSIOIN
        )

    for file in to_install_files:
        copy_file(
            file, sqex_path
        )


def backup_files(sqex_path: str):
    try:
        for file in PATCH_FILES:
            copy_file(
                f'{sqex_path}\\{file}',
                f'{sqex_path}\\{BACKUP_FOLDER_NAME}'
            )
            
    except FileNotFoundError:
        console.print(settings.CLI.INSTALL.backup_failed)
