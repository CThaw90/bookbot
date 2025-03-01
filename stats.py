def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    char_count = {}
    for c in text:
        char = c.lower()
        if char not in char_count:
            char_count[char] = 0

        char_count[char] += 1

    return char_count


def sort_char_count(char_count):
    list_of_dictionaries = [{char: char_count[char]} for char in char_count if char.isalpha()]
    list_of_dictionaries.sort(reverse=True, key=lambda a: a[next(iter(a))])
    return list_of_dictionaries
