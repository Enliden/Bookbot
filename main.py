from stats import count_words, count_characters, sort_char_dict
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents

def main(filepath):
    print("============ BOOKBOT ============")
    
    contents = get_book_text(filepath) 
    print(f"Analyzing book found at {filepath}...")
    
    print("----------- Word Count ----------")
    number_of_words = count_words(contents)
    print(f"Found {number_of_words} total words")
    
    print("--------- Character Count -------")
    char_count = count_characters(contents)
    sorted_char_count = sort_char_dict(char_count)
    for c in sorted_char_count:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
