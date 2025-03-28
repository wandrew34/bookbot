from stats import word_count
from stats import char_count
import sys

def get_book_text(filepath):
    contents = str()
    with open(filepath) as file:
        contents = file.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        book_contents = get_book_text(filepath)
        
        num_words = word_count(book_contents)
        char_dict = char_count(book_contents)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for key in char_dict:
            print(key + ": " + str(char_dict[key]))

main()


