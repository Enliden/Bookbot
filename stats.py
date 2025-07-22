def count_words(content_of_book):
    word_list = content_of_book.split()
    return len(word_list)

def count_characters(content_of_book):
    content_of_book = content_of_book.lower()
    
    num_of_chars = {}
    
    for c in content_of_book:
        if c in num_of_chars:
            num_of_chars[c] += 1
        else:
            num_of_chars[c] = 1    
    return num_of_chars

def sort_char_dict(num_of_chars):
    list = []
    for c in num_of_chars:
        list.append({"char" : c, "num" : num_of_chars[c]})

    def sort_on(dict):
        return dict["num"]

    list.sort(key=sort_on, reverse = True)
    return list
        