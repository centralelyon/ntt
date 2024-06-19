"""TODO : test_delete_and_create_folder ...
"""

from ntt.utils.files import delete_and_create_folder


def test_delete_and_create_folder(sample_path_in):
    """Test delete_and_create_folder function.

    Args:
        sample_path_in (Path): input path
    """
    test_folder = sample_path_in / "test_folder"

    if not test_folder.exists():
        test_folder.mkdir()

    test_file = test_folder / "test_file.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Test")

    new_folder = delete_and_create_folder(test_folder)

    assert new_folder.exists()
    assert not [x for x in new_folder.iterdir()]

    new_folder.rmdir()
