def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_character_count(text)
    list_of_dicts = get_list_of_dicts(chars_dict)
    print()
    print(f"--- Begin report of {path_to_file} ---")
    print()
    print(f"{num_words} words found in the document")
    print()
    list_of_dicts.sort(reverse=True, key=sort_on)
    for item in list_of_dicts:
        print (f"The letter {item['character']} was found {item['count']} times")
    print()
    print("--- End of report ---")
      
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
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def get_list_of_dicts(chars_dict):
    list_of_dicts = []
    for char, count in chars_dict.items():
        new_dict = {"character": char, "count": count}
        list_of_dicts.append(new_dict)
    return list_of_dicts

def sort_on(list_of_dicts):
    return list_of_dicts["count"]
    
main()
