import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
while True:
    try:
        word = input("Enter a word: ").upper()
        if not word.isalpha():
            raise ValueError
    except ValueError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
