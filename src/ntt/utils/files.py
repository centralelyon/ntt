"""TODO : files module provides ...

Not sure those function are really useful.
"""

import os
import shutil
from pathlib import Path


def delete_folder(path):
    """Deletes a folder and all its contents.

    Args:
        path (str or Path): path to the folder to be deleted

    Raises:
        Exception: if the path is not a folder

    Returns:
        bool: True if the folder has been deleted
    """
    folder_path = Path(path)

    if not folder_path.is_dir():
        raise IsADirectoryError(f"Path '{folder_path}' is not a folder")

    shutil.rmtree(folder_path)

    return True


def create_folder(path):
    """Creates a folder if does not exist.

    Args:
        path (str or Path): Folder path
    """
    folder_path = Path(path)

    try:
        folder_path.mkdir()
        print(f"Folder created successfully: {folder_path}")
    except FileExistsError:
        print(f"Folder already exists: {folder_path}")
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")


def delete_and_create_folder(path):
    """Remove folder and its content if nessary and re-creates the folder.

    Args:
        path (str or Path): Folder path

    Returns:
        Path: Path of the folder
    """
    folder_path = Path(path)

    delete_folder(folder_path)
    create_folder(folder_path)

    return folder_path


def copy_file(
    file_path_in, file_name_in, file_path_out, file_name_out, overwrite=False
):
    """Copy source file to destination file.

    Args:
        file_path_in (str or Path): Source file path
        file_name_in (str): Source file name
        file_path_out (str or Path): Destination file path
        file_name_out (str): Destination file name
        overwrite (bool, optional): Overwrites destination file. Defaults to False.
    """
    source_file = Path(file_path_in) / file_name_in
    destination_file = Path(file_path_out) / file_name_out

    if destination_file.exists() and not overwrite:
        raise FileExistsError(f"File '{destination_file}' already exists.")

    shutil.copyfile(source_file, destination_file)

    print(f"File '{file_name_in}' copied to '{destination_file}' successfully.")


def remove_file_if_exists(path):
    """Remove a file if it exists.

    Args:
        path (str or Path): The file path of the file to be removed.

    Returns:
        bool: True if removed
    """
    filepath = Path(path)

    if filepath.exists():
        filepath.unlink()
        print(f"File {filepath} removed successfully.")
        return True
    else:
        print(f"File {filepath} does not exist, not removed.")
        return False


def generate_shortcut_url(path="file.url", url="https://www.google.com"):
    """_summary_

    TODO : aim of this function ?

    Args:
        file_path (str or Path, optional): _description_. Defaults to "file.url".
        url (str, optional): _description_. Defaults to "https://www.google.com".

    Returns:
        _type_: _description_
    """
    file_path = Path(path)

    file_contents = f"""[{{000214A0-0000-0000-C000-000000000046}}]
Prop3=19,2
[InternetShortcut]
URL={url}
IDList=
HotKey=0"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_contents)

    return file_path


def touch(path):
    """Create an empty file or update the file's timestamp.

    TODO : Why raising an error when the file does not exist,
    it is not the way the touch utility works ?

    Args:
        path (str or Path): File path
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} not found")

    with open(file_path, "a", encoding="utf-8"):
        os.utime(file_path, times=None)
        
