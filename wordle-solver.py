import re

def main():
    print ("Enter q after 'Give word' to end and c to clear the excluded letters list")
    print("Give language (d/e)")
    language = input()
    exclude = ""
    while True:
        print("Give word")
        word = input()

        if word.lower() == "q":
            break
        elif word.lower() == "c":
            exclude = ""
            continue

        print("Give excluded letters")
        exclude += input()

        print("Give included letters")
        include = input()

        english_words = load_words(len(word), language)
        for english_word in english_words:
            if re.match(word, english_word) and hasntLetters(exclude, english_word, word) and hasLetters(include, english_word, word):
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

def hasLetters(letters, word, input_word):
    # Split character and position pairs
    letter_list = letters.split()

    # Loop through every character position pairs
    for letter_position in letter_list:
        # Loop through the positions
        for character in letter_position:
            # If the char is a letter this is our letter
            if character.isalpha():
                letter = character
                # If the included character isn't in the word except for its positions in the input_word, return false
                pos1 = getLetterCount(word, letter)
                pos2 = getLetterCount(input_word, letter)
                if not pos1 > pos2:
                    return False
            else:
                if word[int(character) - 1] == letter:
                    return False
    return True

# Returns true if the word doesn't contain the letter not counting the occurances in the input_word. 
def hasntLetters(letters, word, input_word):
    for letter in letters:
        input_count = 0
        count = 0
        if letter in input_word:
            for input_letter in input_word:
                if letter == input_letter:
                    input_count = input_count + 1
            for word_letter in word:
                if letter == word_letter:
                    count = count + 1
            if count > input_count:
                return False
            else:
                return True
        elif letter in word:
            return False
    return True

# Get the occurance count of a letter in a word
def getLetterCount(word, letter):
    pos_list = []
    count = 0
    for char in word:
        if char == letter:
            pos_list.append(count)
        count = count + 1
    return len(pos_list)

main()