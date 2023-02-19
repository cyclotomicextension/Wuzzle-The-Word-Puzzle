import enchant
import numpy as np
from colorama import Fore
import pandas as pd
import random

data=pd.read_csv("https://copylists.com/downloads/words/5_letter_words/5_letter_words.csv", header=None)
word_list=np.array(data[1])
t=random.randint(1,490)
for k in range(5):
  input_word = input(Fore.WHITE + "Enter your 5 letter word: ")
  d = enchant.Dict("en_US")
  len_inword = len(input_word)
  if len_inword != 5 or not d.check(input_word):
    input_word = input("Enter another word.")
  actual_word = word_list[t]
  if input_word == actual_word:
    print("Well done!")
    print("Guessed right in " + str(k)+"/5")
    break
  else:
    for i in range(len(input_word)):
        if i < len(actual_word) and input_word[i] == actual_word[i]:
            print(Fore.GREEN + input_word[i], end="")
        elif input_word[i] in actual_word:
            print(Fore.YELLOW + input_word[i], end="")
        else:
            print(Fore.RED + input_word[i], end="")
    print()  # print a new line after coloring the word
  if k==4:
    print("Exhausted Attempts!")
    print(Fore.WHITE + "The word was "+actual_word)
