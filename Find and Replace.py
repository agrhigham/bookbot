def main():
    path_to_file = "books/code.txt"
    text = get_book_text(path_to_file)
    words = get_words(text)
    target = "test"
    find_word_in_text(words, target)

def get_book_text(path_to_file):
    with open(path_to_file)as f:
        return f.read()
    
def get_words(text):
    words = text.split()
    return words

def find_word_in_text(words, target):
    count = 0
    for word in words:
        if word == target:
            count += 1
    print(count)

main ()
