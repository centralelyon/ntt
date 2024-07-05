# pylint: disable=C0114

import json
import os
from pathlib import Path

import dotenv
from ntt.utils.json_to_text import recursive_json

# https://peps.python.org/pep-0008/#constants
JSON_FILE_NAME = "org_jtt.json"
TEXT_FILE_NAME = "res_jtt.txt"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    json_file = path_in / JSON_FILE_NAME
    text_file = path_out / TEXT_FILE_NAME

    # Upload json data from file
    with json_file.open("r") as f:
        data = json.load(f)

    text_data = recursive_json(data)

    # Write formatted data in text file
    with text_file.open("w") as f:
        f.write(text_data)
