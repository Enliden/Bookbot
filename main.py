from stats import count_words

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
        return contents

def main():
    contents = get_book_text("books/frankenstein.txt") 
    number_of_words = count_words(contents)
    print(f"{number_of_words} words found in the document")

main()
