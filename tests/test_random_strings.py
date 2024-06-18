"""TODO : test_random_strings ...
"""

import string

from ntt.utils.strings import generate_random_string, generate_uuid4


def test_generate_random_string():
    """_summary_
    """
    asked_length = 123
    random_string = generate_random_string(length=asked_length)

    assert len(random_string) == asked_length

    assert all(char in string.ascii_letters + string.digits for char in random_string)


def test_generate_random_uuid():
    """_summary_
    """
    generated_uuid = generate_uuid4()
    split = generated_uuid.split("-")
    assert len(split) == 5


if __name__ == "__main__":
    # TODO : Remove this block
    test_generate_random_string()
    test_generate_random_uuid()
