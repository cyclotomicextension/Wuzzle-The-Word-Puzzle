# Wuzzle-The-Word-Puzzle

**Overview**

Wuzzle is a simple command-line word-guessing game written in Python. It prompts the user to enter a 5-letter word and compares it to a randomly selected word from a list of five-letter words. If the guessed word matches the selected word, the game ends. Otherwise, the program gives feedback on the letters in the guessed word that match the selected word and prompts the user to guess again.

**Dependencies**

Wuzzle requires the following dependencies to run:

enchant

numpy

colorama

pandas

Installation of dependencies can be done using pip, the Python package manager.

**Usage**

To run the Wuzzle game, open a command prompt or terminal and navigate to the directory containing the Wuzzle Python file. Then enter the following command:
`python wuzzle.py`

**Gameplay**

Wuzzle will randomly select a 5-letter word from a list of five-letter words.

The user will be prompted to enter a 5-letter word.

If the word entered is not a valid English word, the user will be prompted to enter another word.

If the word entered is a valid English word but not 5 letters long, the user will be prompted to enter another word.

If the word entered is a valid English word and 5 letters long, the program will compare the word to the randomly selected word.

If the guessed word matches the selected word, the game ends and the user is declared the winner.

If the guessed word does not match the selected word, the program will give feedback on the letters in the guessed word that match the selected word and prompt the user to guess again.

The user will have 5 attempts to guess the word. If they do not guess the word correctly in 5 attempts, the game ends and the selected word is displayed.

**Output**

The output of Wuzzle is printed to the console. The feedback on the guessed word is color-coded using the colorama library, with green letters indicating correct letters in the correct position, yellow letters indicating correct letters in the wrong position, and red letters indicating incorrect letters. If the user exhausts all 5 attempts, the correct word is displayed in white.
