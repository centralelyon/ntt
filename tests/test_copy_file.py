"""TODO : test_copy_file ...
"""

import os
import shutil

from dotenv import load_dotenv
from ntt.utils.files import copy_file


def test_copy_file():
    """_summary_
    """
    load_dotenv()
    temp_dir = os.path.join(str(os.environ.get("FRAME_PATH_OUT")), "temp_dir_copy_file")

    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)

    file_name_in = "original_file.txt"
    original_file = os.path.join(temp_dir, file_name_in)

    with open(original_file, "w", encoding="utf-8") as f:
        f.write("This is a test file.")

    destination_dir = os.path.join(temp_dir, "destination")

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    file_name_out = "copied_file.txt"

    copy_file(temp_dir, file_name_in, destination_dir, file_name_out)

    destination_file = os.path.join(destination_dir, file_name_out)
    assert os.path.exists(destination_file)

    with open(destination_file, "r", encoding="utf-8") as f:
        assert f.read() == "This is a test file."

    os.remove(original_file)
    os.remove(destination_file)

    assert not os.path.exists(original_file)
    assert not os.path.exists(destination_file)

    shutil.rmtree(temp_dir, ignore_errors=True)
