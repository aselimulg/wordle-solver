from operator import contains
import re

def main():
    while True:
        print("Give word")
        word = input()
        print("Give excluded letters")
        exclude = input()

        print("Give included letters")
        include = input()

        english_words = load_words(len(word))
        for english_word in english_words:
            if re.match(word, english_word) and hasntLetters(exclude, english_word) and hasLetters(include, english_word):
                print(english_word)

def load_words(length):
    #with open('words-alpha.txt') as word_file:
    with open('wordlist-german.txt') as word_file:

        valid_words = set(word_file.read().split())

    words = set()
    for word in valid_words:
        if len(word) == length:
            words.add(word)

    return words

def hasLetters(letters, word):
    for letter in letters:
        if not letter in word:
            return False
    return True

def hasntLetters(letters, word):
    for letter in letters:
        if letter in word:
            return False
    return True

main()