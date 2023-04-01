import os
import bz2
import shutil
import tarfile


def tar_decompress(source_file_path: str, target_file_path: str = '.') -> None:
    try:
        if not os.path.isfile(source_file_path):
            raise FileNotFoundError("Source file does not exist")
        if not tarfile.is_tarfile(source_file_path):
            raise ValueError("Source file is not a valid tar file")
        if not os.path.isdir(target_file_path):
            raise FileNotFoundError("Target directory does not exist")

        with tarfile.open(source_file_path) as tar_file:
            tar_file.extractall(target_file_path)

    except (FileNotFoundError, PermissionError, tarfile.TarError) as e:
        print(f"Error occurred while extracting tar file: {e}")

def bz2_decompress(source_file_path: str,
                   target_file_path: str,
                   delete_source_file: bool = False) -> None:
    try:
        if not os.path.isfile(source_file_path):
            raise FileNotFoundError("Source file does not exist")
        if not source_file_path.endswith('.bz2'):
            raise ValueError("Source file is not a valid bz2 file")
        if not os.path.isdir(os.path.dirname(target_file_path)):
            raise FileNotFoundError("Target directory does not exist")

        with bz2.open(source_file_path, 'rt', encoding='utf-8') as source_file_obj, \
             open(target_file_path, 'w', encoding='utf-8') as destination_file_obj:
            destination_file_obj.write(source_file_obj.read())

        if delete_source_file:
            os.remove(source_file_path)

    except (FileNotFoundError, PermissionError, ValueError) as e:
        print(f"Error occurred while decompressing file: {e}")

def generate_file_path(root_path: str = '.', extensions: str = None) -> list:
    if not os.path.isdir(root_path):
        raise NotADirectoryError(f"{root_path} is not a valid directory")

    if extensions:
        extensions = extensions.split(';')
        extensions = [ext.strip() for ext in extensions]
        extensions = tuple(extensions)

    file_path_list = [os.path.join(directory_path, file)
                      for directory_path, sub_directory, files in os.walk(root_path)
                      for file in files
                      if not extensions or file.endswith(extensions)]

    return file_path_list

def clean_dir(dir_path: str):
    if not os.path.isdir(dir_path):
        raise NotADirectoryError(f"{dir_path} is not a valid directory")

    try:
        shutil.rmtree(dir_path)
    except FileNotFoundError:
        pass

    os.makedirs(dir_path, exist_ok=True)