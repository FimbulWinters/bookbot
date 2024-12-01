def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    total = count_words(file_contents)
    letter_counts = letter_count(file_contents)
    print_report(letter_counts, total)

def count_words(content):
    number_of_words = len(content.split())
    # print(number_of_words)
    return number_of_words

def letter_count(content):
    allowed = ['a']
    chars ={}

    lowercase = content.lower()

    for char in lowercase:
        if char.isalnum():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    print(chars)
    return chars

def sort_on(dict):
    return dict["num"]


def print_report(dict, total_words):
    print("report")
    char_info = []

    for entry in dict:
        print(entry)
        char_info.append({
            "char": entry,
            "num": dict[entry]
        })
    
    char_info.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words were found in the document \n")
    for item in char_info:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")



main()