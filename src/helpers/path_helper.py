import os
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


async def remove_file(file_path: str, raise_exception=False):
    try:
        await async_os.remove(file_path)
    except FileNotFoundError as e:
        if (raise_exception):
            raise e


def make_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)
