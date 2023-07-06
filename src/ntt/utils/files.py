import os
import shutil


def delete_folder(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)

        os.rmdir(path)


def create_folder(folder_path):
    try:
        os.mkdir(folder_path)
        print(f"Folder created successfully: {folder_path}")
    except FileExistsError:
        print(f"Folder already exists: {folder_path}")
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")


def delete_and_create_folder(path):
    delete_folder(path)
    create_folder(path)
    return path


def copy_file(
    file_path_in, file_name_in, file_path_out, file_name_out, overwrite=False
):
    source_file = os.path.join(file_path_in, file_name_in)
    destination_file = os.path.join(file_path_out, file_name_out)

    if os.path.exists(destination_file) and not overwrite:
        print(f"File '{file_name_out}' already exists.")
        return

    shutil.copy(source_file, destination_file)

    print(f"File '{file_name_in}' copied to '{file_name_out}' successfully.")


def remove_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} removed successfully.")
        return True
    else:
        print(f"File {file_path} does not exist, not removed.")
        return False


def generate_shortcut_url(file_path="file.url", url="https://www.google.com"):
    file_contents = "[{000214A0-0000-0000-C000-000000000046}]\n"
    file_contents += "Prop3=19,2\n[InternetShortcut]\n"
    file_contents += "URL={}\nIDList=\nHotKey=0\n".format(url)
    with open(file_path, "w") as f:
        f.write(file_contents)
    return file_path
