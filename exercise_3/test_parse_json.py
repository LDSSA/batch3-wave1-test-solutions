import io

from parse_json import parse_json


def test_1():
    data = (
        '{"C": 3}\n'
        '{"A": 1, "B": "Hello"}\n'
        '"Blabla"\n'
        '{"C": 76, "A": -14, "B": 7}\n'
        '{"C": "Bla", "D": 34, "B": "This is a string!"}\n'
        '{"B":"A", "A": 50.5}'
    )
    fd = io.StringIO(data)

    assert parse_json(fd) == [-14, 'Hello']


def test_2():
    data = (
        '{"C": 3}\n'
        '{"A": "1", "B": "Hello"}\n'
        '"Blabla"'
    )
    fd = io.StringIO(data)

    assert parse_json(fd) == [None, 'Hello']


def test_3():
    data = (
        '{"C": 3}\n'
        '{"A": "1", "B": 3}\n'
        '"Blabla"'
    )
    fd = io.StringIO(data)

    assert parse_json(fd) == [None, None]
