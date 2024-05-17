def main():
    path_to_file = "books/code.txt"
    text = get_book_text(path_to_file)
    target = "test"
    replacement = "exam"
    new_text = replace_word_in_text(text, target, replacement)
    output_file = "books/modified_code.txt"
    save_new_text(output_file, new_text)

def get_book_text(path_to_file):
    with open(path_to_file)as f:
        return f.read()

def replace_word_in_text(text, target, replacement):
    words = text.split()
    new_words = []
    for word in words:
        if word.lower() == target.lower():
            new_words.append(replacement)
        else:
            new_words.append(word)
    return ' '.join(new_words)

def save_new_text(path_to_file, text):
    with open(path_to_file, 'w') as f:
        f.write(text)

main()
