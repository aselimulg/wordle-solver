# wordle-solver
## A script to solve wordles
This script iterates through all the words in the given languages and prints out the words that match the given wordle requirements.

## How To Use
At first you pick the language of the word. (Right now only English and German) . You will then be prompted to give the wordle word. If you don't know which letter is in a position, you type `.` instead of that letter. If you don't know any letter in the word that is for example five letters long, you type `.....`. 

After that you will be prompted to give the letters that are not in the wordle word. The script saves the excluded letters so you don't have to type them after every single guess. If a letter is guessed multiple times in one guess and the wordle doesn't contain that letter guessed amount of times, if you have typed letter in the first part, you can put the same letter in excluded letters part to search for words that has that letter that amount of times. 

For example if the word is `a_d` and you know there is not another d, you can type d in the excluded letters part so the script only shows you the words with no second d in it.

Finally you will be asked to type the included letters. You have to type the letter first and without any space in between type the positions in which the letter is not in and seperate these letter-position groups, with a space in between. If the word contains multiple occurances of the letter the script will show you the words with that amount of occurances.

Example 

`_ _ _ _ _`

- a is not in 3rd and 4th positions

- e is not in 2nd position

so, for included letters you type:
`a34 e2`

The script will show you all the compatible words.
