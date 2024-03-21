import pandas as pd

nato = pd.read_csv("Day26 - Nato Alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for _, row in nato.iterrows()}
word = input("Enter word: ")
print([nato_dict[letter.upper()] for letter in word])
