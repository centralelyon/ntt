import os
import json


def generate_index(folder_path, index_filename="index.json", max_depth=None):
    """Generates an index JSON file for all folders and files in the given folder.

    Args:
        folder_path (str): Path to the input folder.
        index_filename (str): Name of the index JSON file. Default is "index.json".
        max_depth (int or None): Maximum depth of recursion. None for unlimited depth.

    Returns:
        None
    """
    index = []

    for root, _, files in os.walk(folder_path):
        if max_depth is not None:
            depth = root[len(folder_path) :].count(os.sep)
            if depth > max_depth:
                continue

        for name in files:
            entry = {"type": "file", "path": os.path.join(root, name), "name": name}
            index.append(entry)

    for root, _, dirs in os.walk(folder_path):
        if max_depth is not None:
            depth = root[len(folder_path) :].count(os.sep)
            if depth > max_depth:
                continue

        for name in dirs:
            entry = {"type": "folder", "path": os.path.join(root, name), "name": name}
            index.append(entry)

    with open(index_filename, "w") as json_file:
        json.dump(index, json_file, indent=4)


# Replace '/path/to/folder' with the actual folder path
# Provide the desired index file name and maximum depth if needed
if __name__ == "__main__":
    generate_index(".", index_filename="custom_index.json", max_depth=2)
