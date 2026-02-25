import json


def pretty_json(path_json):
    """Open the same file for writing, and write the pretty-printed JSON to disk.

    Args:
        path_json (_type_): _description_

    Raises:
        FileNotFoundError: _description_

    Returns:
        _type_: _description_
    """
    try:
        with open(path_json, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File {path_json} not found")
        return

    try:
        with open(path_json, "w") as f:
            json.dump(data, f, indent=4, sort_keys=True)
    except FileNotFoundError:
        print(f"File {path_json} not found")
        return


def get_index(list_dict, key, value):
    """Get the index of a dictionary in a list of dictionaries

    Args:
        list_dict (_type_): _description_
        key (_type_): _description_
        value (_type_): _description_

    Returns:
        _type_: _description_
    """

    for i, item in enumerate(list_dict):
        if item.get(key) == value:
            return i
    return None
