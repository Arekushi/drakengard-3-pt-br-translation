import os
import shutil
from aiofiles import os as async_os


def has_folder(folder_path: str) -> bool:
    return os.path.exists(folder_path)


def has_file(file_path: str) -> bool:
    return os.path.isfile(file_path)


def get_all_files(path: str) -> list[str]:
    files = [
        os.path.join(parent, name)
        for (parent, subdirs, files) in os.walk(path)
        for name in files
        if os.path.isfile(os.path.join(parent, name))
    ]

    return files


def update_dir(file_path: str, new_dir: str) -> str:
    file_name, file_ext = os.path.splitext(file_path)
    new_file_path = os.path.join(new_dir, os.path.basename(file_name) + file_ext)
    
    return new_file_path


def make_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def copy_file(file_path, dest_path):
    make_dir(dest_path)
    return shutil.copy(file_path, dest_path)


def delete(path):
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError(f"file {path} is not a file or dir.")
