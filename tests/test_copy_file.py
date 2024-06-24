"""TODO : test_copy_file ...
Using pytest tmp_path fixture : https://docs.pytest.org/en/8.2.x/how-to/tmp_path.html
"""

from ntt.utils.files import copy_file


def test_copy_file(tmp_path):
    """Test ntt copy_file function.

    Args:
        tmp_path (Path): pytest temporary directory fixture
    """
    file_name_in = "original_file.txt"
    original_file = tmp_path / "original_file.txt"

    with open(original_file, "w", encoding="utf-8") as f:
        f.write("This is a test file.")

    file_name_out = "copied_file.txt"

    copy_file(tmp_path, file_name_in, tmp_path, file_name_out)

    destination_file = tmp_path / "copied_file.txt"

    assert destination_file.exists()

    with open(destination_file, "r", encoding="utf-8") as f:
        assert f.read() == "This is a test file."
