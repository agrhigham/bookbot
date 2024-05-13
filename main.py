def main():
    
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars_dict = get_character_count(text)
    print (chars_dict)
   
   
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path_to_file):
    with open(path_to_file)as f:
        return f.read()
    
def get_character_count(text):
    character_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
    






main()
