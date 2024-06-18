"""TODO : files module provides ...
"""

import os
import shutil


def delete_folder(path: str):
    """Deletes a folder and all its contents.

    Args:
        path (str): path to the folder to be deleted

    Raises:
        Exception: if the path is not a folder

    Returns:
        str: path to the deleted folder
    """

    if not os.path.isdir(path):
        raise Exception(f"Path '{path}' is not a folder.")

    if os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)

            for directory in dirs:
                dir_path = os.path.join(root, directory)
                os.rmdir(dir_path)

        os.rmdir(path)

    return path


def create_folder(folder_path):
    """_summary_

    Args:
        folder_path (_type_): _description_
    """
    try:
        os.mkdir(folder_path)
        print(f"Folder created successfully: {folder_path}")
    except FileExistsError:
        print(f"Folder already exists: {folder_path}")
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")


def delete_and_create_folder(path):
    """_summary_

    Args:
        path (_type_): _description_

    Returns:
        _type_: _description_
    """
    delete_folder(path)
    create_folder(path)
    return path


def copy_file(
    file_path_in, file_name_in, file_path_out, file_name_out, overwrite=False
):
    """_summary_

    Args:
        file_path_in (_type_): _description_
        file_name_in (_type_): _description_
        file_path_out (_type_): _description_
        file_name_out (_type_): _description_
        overwrite (bool, optional): _description_. Defaults to False.
    """
    source_file = os.path.join(file_path_in, file_name_in)
    destination_file = os.path.join(file_path_out, file_name_out)

    if os.path.exists(destination_file) and not overwrite:
        print(f"File '{file_name_out}' already exists.")
        return

    shutil.copy(source_file, destination_file)

    print(f"File '{file_name_in}' copied to '{file_name_out}' successfully.")


def remove_file_if_exists(file_path):
    """_summary_

    Args:
        file_path (_type_): _description_

    Returns:
        _type_: _description_
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} removed successfully.")
        return True
    else:
        print(f"File {file_path} does not exist, not removed.")
        return False


def generate_shortcut_url(file_path="file.url", url="https://www.google.com"):
    """_summary_

    Args:
        file_path (str, optional): _description_. Defaults to "file.url".
        url (str, optional): _description_. Defaults to "https://www.google.com".

    Returns:
        _type_: _description_
    """
    file_contents = "[{000214A0-0000-0000-C000-000000000046}]\n"
    file_contents += "Prop3=19,2\n[InternetShortcut]\n"
    file_contents += f"URL={url}\nIDList=\nHotKey=0\n"
    with open(file_path, "w") as f:
        f.write(file_contents)
    return file_path


def touch(file_path):
    """Create an empty file or update the file's timestamp.

    Args:
        file_path (_type_): _description_

    Raises:

    """
    # raise an error if the file does not exist
    try:
        with open(file_path, "a"):
            os.utime(file_path, times=None)
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return
