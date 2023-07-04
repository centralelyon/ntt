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


def delete_and_create_folder(path):
    delete_folder(path)
    os.mkdir(path)
    return path


def copy_file(file_path, file_path_out):
    print("copy files", file_path, file_path_out)

    if os.path.exists(file_path):
        shutil.copyfile(file_path, file_path_out)
        print(f"File {file_path} copied successfully.")
    else:
        print(f"File {file_path} does not exist.")

    return file_path_out


def remove_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} removed successfully.")
        return True
    else:
        print(f"File {file_path} does not exist, not removed.")
        return False
