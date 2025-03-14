import os
import zipfile
from src.helpers.path_helper import has_file


def zip_folder(zip_name, folder_path, destination_path):
    zip_full_path = os.path.join(destination_path, zip_name)
    
    with zipfile.ZipFile(zip_full_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        for folder_name, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                arcname = os.path.relpath(file_path, folder_path)
                zip_ref.write(file_path, arcname=arcname)

    return zip_full_path


def unzip_file(zip_file_path, extract_path):
    if has_file(zip_file_path):
        zip_file_obj = zipfile.ZipFile(zip_file_path)
        zip_file_obj.extractall(extract_path)
        zip_file_obj.close()
