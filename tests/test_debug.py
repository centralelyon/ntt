from ntt.utils.debug import debug


def test_multiple_strings(capsys):
    debug("Hello", "world")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello world"


def test_mixed_types(capsys):
    debug("Hellow world", 42, True)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hellow world 42 True"


def test_no_arguments(capsys):
    debug()
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


def test_nested_structure(capsys):
    debug([1, 2, 3], {"a": 1}, (4, 5))
    captured = capsys.readouterr()
    assert captured.out.strip() == "[1, 2, 3] {'a': 1} (4, 5)"
