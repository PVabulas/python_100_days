from faker import Faker
import hangman_art as art

stages = art.stages
logo = art.logo
fake = Faker()

print(logo)

word = fake.word().lower()
num_letters = len(word)
lives = 6
state = []
for letter in word:
    state.append("_")
guessed_letters = []

print(f"Welcome to Hangman, the word has {num_letters} letters.")

while ("_" in state) and (lives > 0):
    guess = input("Choose a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed the letter {guess}")
    else:
        in_word = False
        for i, letter in enumerate(word):
            if letter == guess:
                state[i] = guess
                in_word = True
        if not in_word:
            print(f"The letter {guess} is not in the word, life lost.")
            lives -= 1
        guessed_letters.append(guess)
    print(" ".join(state))
    print(stages[lives])
if lives == 0:
    print("You're dead!")
else:
    print("You win!")
