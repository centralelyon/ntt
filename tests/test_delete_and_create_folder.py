import os
from dotenv import load_dotenv
from ntt.utils.files import delete_and_create_folder


def test_delete_and_create_folder():
    load_dotenv()
    test_path_in = os.environ.get("VIDEO_PATH_IN")
    test_folder = os.path.join(test_path_in, "test_folder")
    if not os.path.exists(test_folder):
        os.mkdir(test_folder)

    test_file = os.path.join(test_folder, "test_file.txt")
    with open(test_file, "w") as file:
        file.write("Test")

    new_folder = delete_and_create_folder(test_folder)

    assert os.path.exists(new_folder)
    assert not os.listdir(new_folder)

    os.rmdir(new_folder)


if __name__ == "__main__":
    test_delete_and_create_folder()
