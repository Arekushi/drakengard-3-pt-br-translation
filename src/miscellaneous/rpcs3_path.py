from rich.console import Console
from config import settings, ROOT_DIR
from src.helpers.path_helper import get_all_files, has_folder

from dynaconf.loaders.toml_loader import write
from dynaconf.vendor.box.exceptions import BoxKeyError


console = Console()
RPCS3_REQUIRED_FILES = settings.FILES.rpcs3_required_files
TOMLS_PATH = f'{ROOT_DIR}\\{settings.DEFAULT_PATHS.tomls}'
SECRET_FILE = settings.FILES.secret_file
D3_VERSIONS = settings.D3.versions
D3_SQEX03GAME_PATH = settings.DEFAULT_PATHS.d3_sqex03game


def ensure_sqe3x0game_path():
    if not has_sqe3x0game_path():
        console.print(settings.CLI.RPCS3_PATH.not_found)
        input_rpcs3_path()


def input_rpcs3_path():
    while True:
        new_path = console.input(settings.CLI.RPCS3_PATH.write_path)
        
        if is_rpcs3_valid_path(new_path):
            sqex0game_path = get_s3ex03game_path(new_path)
            
            if sqex0game_path:
                write_sqe3x0game_path(sqex0game_path)
                break
            else:
                console.print(settings.CLI.RPCS3_PATH.d3_error)
                continue
        
        console.print(settings.CLI.RPCS3_PATH.path_error)
        
        for i, file in enumerate(RPCS3_REQUIRED_FILES):
            console.print(f'{i + 1}. [b]{file}[/b]')
        console.print()


def write_sqe3x0game_path(
    d3_sqex03game_path: str,
):
    obj = {
        'PATHS': {
            'SQEX03GAME_path': d3_sqex03game_path
        }
    }
    
    write(F'{TOMLS_PATH}\\{SECRET_FILE}', obj, merge=True)
    settings.update(obj)


def has_sqe3x0game_path():
    try:
        return has_folder(settings.PATHS.SQEX03GAME_path)
    except (BoxKeyError, AttributeError):
        return False


def is_rpcs3_valid_path(path: str) -> bool:
    files = get_all_files(path)
    files = [file.split('\\')[-1] for file in files]
    has_required_files = set(RPCS3_REQUIRED_FILES).issubset(set(files))
    return has_required_files


def get_s3ex03game_path(rpcs3_path: str):    
    for version in D3_VERSIONS:
        full_path = f"{rpcs3_path}\\{str(D3_SQEX03GAME_PATH).replace('<version>', version)}"
        
        if has_folder(full_path):
            return full_path
    
    return None
