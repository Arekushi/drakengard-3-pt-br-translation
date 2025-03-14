import os
import requests
from rich.console import Console

from src.helpers.path_helper import make_dir

console = Console()


def download_file(
    url: str,
    dest_path: str,
    chunk_size: int = 8192
):
    file_name = os.path.basename(url) 
    file_path = os.path.join(dest_path, file_name)

    try:
        make_dir(dest_path)

        with requests.get(url, stream=True) as response:
            response.raise_for_status()

            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        file.write(chunk)

        return file_path
    except requests.RequestException as e:
        console.print(f"Erro ao baixar {url}: {e}")
        return None
    except IOError as e:
        console.print(f"Erro ao salvar o arquivo {file_path}: {e}")
        return None
