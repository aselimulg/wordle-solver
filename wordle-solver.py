import re

def main():
    print("Give language (d/e)")
    language = input()
    while True:
        print("Give word")
        word = input()
        print("Give excluded letters")
        exclude = input()

        print("Give included letters")
        include = input()

        english_words = load_words(len(word), language)
        for english_word in english_words:
            if re.match(word, english_word) and hasntLetters(exclude, english_word) and hasLetters(include, english_word):
                print(english_word)

def load_words(length, language):
    if language.startswith("e"):
        with open('words-alpha.txt') as word_file:
            valid_words = set(word_file.read().split())
    else:
        with open('wordlist-german.txt') as word_file:
            valid_words = set(word_file.read().split())

    words = set()
    for word in valid_words:
        if len(word) == length:
            words.add(word)

    return words

def hasLetters(letters, word):
    letter_list = letters.split()
    for letter_position in letter_list:
        for character in letter_position:
            if character.isalpha():
                letter = character
                if letter not in word:
                    return False
            else:
                if word[int(character) - 1] == letter:
                    return False
    return True

def hasntLetters(letters, word):
    for letter in letters:
        if letter in word:
            return False
    return True

main()