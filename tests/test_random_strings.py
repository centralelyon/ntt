import string
from ntt.utils.strings import generate_random_string, generate_uuid4


def test_generate_random_string():
    l = 123
    random_string = generate_random_string(length=l)

    assert len(random_string) == l

    assert all(char in string.ascii_letters + string.digits for char in random_string)


def test_generate_random_uuid():
    generated_uuid = generate_uuid4()
    split = generated_uuid.split("-")
    assert len(split) == 5


if __name__ == "__main__":
    test_generate_random_string()
    test_generate_random_uuid()
