# pylint: disable=C0114

import json
import os
from pathlib import Path

import dotenv
from ntt.utils.text_to_json import text_to_json

# https://peps.python.org/pep-0008/#constants
TEXT_FILE_NAME = "org_ttj.txt"
JSON_FILE_NAME = "res_ttj.json"

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    text_file = path_in / TEXT_FILE_NAME
    json_file = path_out / JSON_FILE_NAME

    # Load data from text file
    # TODO : convert the text file to utf-8 ?
    with text_file.open("r", encoding="latin-1") as f:
        data = f.read()

    json_data = text_to_json(data)

    # Write json data to file
    with json_file.open("w") as f:
        json.dump(json_data, f)
