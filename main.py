def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    count_words(file_contents)
    letter_count(file_contents)

def count_words(content):
    number_of_words = len(content.split())
    print(number_of_words)
    return number_of_words

def letter_count(content):
    chars ={}

    lowercase = content.lower()

    for char in lowercase:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    print(chars)
    return chars




main()