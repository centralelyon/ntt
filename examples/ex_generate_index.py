"""Example of invocation of generate_index to get a
listing of folder and subfolder elements.
"""

import os
from pathlib import Path

import dotenv
from ntt.utils.generate import generate_index


# https://peps.python.org/pep-0008/#constants
JSON_FILE_1 = "src_ntt_maxdepth_2.json"
JSON_FILE_2 = "src_ntt_all.json"
MAX_DEPTH = 2
EXCLUDE_FOLDERS = [".git", ".venv", ".vscode", "__pycache__"]

if __name__ == "__main__":
    ev_path_parent = Path(dotenv.find_dotenv()).parent

    dotenv.load_dotenv()

    path_in = Path(ev_path_parent / os.environ.get("PATH_IN"))
    path_out = Path(ev_path_parent / os.environ.get("PATH_OUT"))

    # Replace '/path/to/folder' with the actual folder path
    # Provide the desired index file name and maximum depth if needed
    generate_index(
        ".", path_out, index_filename=JSON_FILE_1, max_depth=MAX_DEPTH
    )

    # One can exclude a list of folders and no max_depth limit
    generate_index(
        ".", path_out, EXCLUDE_FOLDERS, index_filename=JSON_FILE_2, max_depth=None
    )
