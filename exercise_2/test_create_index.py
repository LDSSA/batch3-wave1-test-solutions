from create_index import create_index


def test_1():
    lst = ["Salut!", 9, 7.5, [1, 2, 3], "bye", "tomat0", "surpr!se", 13, None]

    answer = create_index(lst)
    assert answer == {"S": ["surprse", "salut"], "B": ["bye"], "T": ["tomat"]}


def test_2():
    lst = []

    answer = create_index(lst)
    assert answer == {}


def test_3():
    lst = ["alice!", '9', 'BOB', None, 'berlim', 'Charlie']

    answer = create_index(lst)
    assert answer == {"A": ["alice"], "B": ["bob", "berlim"], "C": ["charlie"]}
