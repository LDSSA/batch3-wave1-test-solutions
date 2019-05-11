import re


def clean_word(word):
    char_list = [c for c in word if ('a' <= c <= 'z') or ('A' <= c <= 'Z')]

    return ''.join(char_list)


def clean_word_with_regex(string):
    return ''.join(re.findall("[a-zA-Z]+", word))


def sort_lists(word_dict):
    for idx in word_dict.keys():
        word_dict[idx].sort(reverse=True)


def add_word_to_dict(word_dict, word):
    if word == '':
        return

    idx = word[0].upper()
    word_lower = word.lower()

    try:
        word_dict[idx].append(word_lower)
    except KeyError:
        word_dict[idx] = [word_lower]


def create_index(lst):
    word_dict = {}

    for word in lst:
        if not isinstance(word, str):
            continue

        # clean_word() can be replaced by clean_word_with_regex()
        word = clean_word(word)
        add_word_to_dict(word_dict, word)

    sort_lists(word_dict)

    return word_dict
