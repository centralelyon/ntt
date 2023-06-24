import json


def pretty_json(path_json):
    """open the same file for writing, and write the pretty-printed JSON"""
    with open(path_json, "r") as f:
        data = json.load(f)

    with open(path_json, "w") as f:
        json.dump(data, f, indent=4, sort_keys=True)


def get_index(list_dict, key, value):
    """helper to get index of a key in a json file"""
    for i in range(len(list_dict)):
        if list_dict[i][key] == value:
            return i
