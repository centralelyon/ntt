"""generates module contains function to generate an index JSON file
for all folders and files in a given folder.
"""

import json
from pathlib import Path


def walk_folder_content(folder, base_folder, exclude_folders, max_depth):
    """Walk the folder recursively to list the content
    until max_depth is reached.

    Each element of the folder is described in a dictionary.

    Args:
        folder (Path): Current folder listed
        base_folder (Path): Base = start folder, used to get relative path
        exclude_folders (list of str): List of folder names to ignore.
        max_depth (int): Max depth for recursion

    Returns:
        list of dict: List current folder (and subfolders) elements.
    """
    content = []

    folder_path = Path(folder)

    for p in folder_path.glob("*"):
        relative_path = p.relative_to(base_folder)
        depth = len(relative_path.parts)

        elt = {
            "path": str(relative_path),
            "name": p.name,
            "depth": depth,
        }

        if p.is_file():
            elt["type"] = "file"
            content.append(elt)

        if exclude_folders is not None and p.name in exclude_folders:
            continue

        if p.is_dir():
            elt["type"] = "folder"
            content.append(elt)

            if depth <= max_depth:
                sublist = walk_folder_content(
                    p, base_folder, exclude_folders, max_depth
                )
                content.extend(sublist)

    return content


def walk_without_limit(folder, base_folder, exclude_folders):
    """Get all folder and subfolder content without depth limit.
    This function is not recursive, it uses Path.rglob() to get all content.

    Args:
        folder (Path): Current folder listed
        base_folder (Path): Base = start folder, used to get relative path
        exclude_folders (list of str): List of folder names to ignore.

    Returns:
        list of dict: List current folder (and subfolders) elements.
    """
    content = []

    folder_path = Path(folder)

    for p in folder_path.rglob("*"):
        # rglob is easy to use but has no mechanism to exclude folders
        if exclude_folders is not None:
            skip = False

            for ef in exclude_folders:
                if ef in p.parts:
                    skip = True

            if skip:
                continue

        relative_path = p.relative_to(base_folder)
        depth = len(relative_path.parts)

        elt = {
            "path": str(relative_path),
            "name": p.name,
            "depth": depth,
        }

        if p.is_file():
            elt["type"] = "file"

        if p.is_dir():
            elt["type"] = "folder"

        content.append(elt)

    return content


def generate_index(
    input_path,
    output_path,
    exclude_folders=None,
    index_filename="index.json",
    max_depth=None,
):
    """Generates an index JSON file for all folders and files in the given folder.

    Args:
        input_path (str or Path): Path to the input folder.
        output_path (str or Path): Path to the output folder.
        exclude_folders (list of str): List of folder names to ignore.
        index_filename (str): Name of the index JSON file. Default is "index.json".
        max_depth (int or None): Maximum depth of recursion. None for unlimited depth.

    Returns:
        None
    """
    index = []

    folder_path = Path(input_path).resolve()

    if max_depth is None:
        lfc = walk_without_limit(folder_path, folder_path, exclude_folders)
    else:
        lfc = walk_folder_content(folder_path, folder_path, exclude_folders, max_depth)

    index.extend(lfc)

    json_file = Path(output_path) / index_filename

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)
