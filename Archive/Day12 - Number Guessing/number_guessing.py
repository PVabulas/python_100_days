# Easy or hard mode
# Easy has 10 attempts
# Hard has 5 attempts
# Ask for a guess
# Say if guess is too high, too low, or spot-on
# If not spot-on, reduce attempts by 1
# If out of attempts, lose
from time import sleep
from random import randint

logo = """  ________                                 _  _   
 /  _____/ __ __   ____   ______ ______ __| || |__
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __   /
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  ||  | 
 \______  /____/  \___  >____  >____  > /_  ~~  _\
        \/            \/     \/     \/    |_||_|  
"""


def number_guessing():
    print(logo)
    sleep(0.5)
    print("Welcome to the guessing game.")
    sleep(0.5)
    while True:
        game()
        if (input("Would you like another game? Y/N\n")) == "N":
            break
    print("Thanks for playing, goodbye.")
    sleep(0.5)


def game():
    mode = input("Would you like to play in (E)asy or (H)ard mode?\n").lower()
    answer = randint(1, 100)
    lives = 5
    if mode == "e":
        lives += 5
    while lives > 0:
        if lives == 1:
            print(f"This is your last attempt.")
            sleep(0.5)
        else:
            print(f"You have {lives} attempts remaining.")
            sleep(0.5)
        if guess(answer) == "Correct":
            print("Congratulations, you guessed correctly.")
            sleep(0.5)
            return
        else:
            lives -= 1
    print("You are out of attempts. You lose!")
    sleep(0.5)


def guess(answer):
    choice = int(input("Pick a number between 1 and 100: "))
    if choice > answer:
        print("Too high")
        sleep(0.5)
        return "Wrong"
    elif choice < answer:
        print("Too low")
        sleep(0.5)
        return "Wrong"
    else:
        return "Correct"


number_guessing()
