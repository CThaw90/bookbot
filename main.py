from stats import get_num_words, get_char_count, sort_char_count

import sys


def get_book_text(file_path):
    with open(file_path) as book_file:
        file_contents = book_file.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = sort_char_count(char_count)
    
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for count in sorted_char_count:
        key = next(iter(count))
        print(f'{key}: {count[key]}')

    print('============= END ===============')

main()
