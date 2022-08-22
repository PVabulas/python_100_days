import art
import game_data
from time import sleep
from random import choice


def higher_or_lower():
    print(art.logo)
    sleep(0.5)
    print("Welcome to Higher or Lower")
    sleep(0.5)
    print("Let's play a game")
    sleep(0.5)
    while True:
        play_game()
        if input("Would you like to play another game? Y/N\n") == "N":
            break
    print("Thanks for playing, goodbye.")
    sleep(0.5)


def play_game():
    score = 0
    a = None
    while True:
        a, b = give_options(a)
        choice = input("Which has the most followers? A or B\n")
        is_correct, a = check_correct(choice, a, b)
        if is_correct:
            print("Correct, you score a point")
            sleep(0.5)
            score += 1
            print(f"Current score: {score}")
            sleep(0.5)
        else:
            print(f"Incorrect, game over. You've scored {score} points.")
            sleep(0.5)
            break


def give_options(a=None):
    if a == None:
        a = choice(game_data.data)
    b = choice(game_data.data)
    print(
        f"Your first option is {a['name']}, they are a {a['description']} from {a['country']}"
    )
    sleep(0.5)
    print(art.vs)
    sleep(0.5)
    print(
        f"Your second option is {b['name']}, they are a {b['description']} from {b['country']}"
    )
    sleep(0.5)
    return a, b


def check_correct(choice, a, b):
    if a["follower_count"] > b["follower_count"]:
        winner = ("A", a)
    elif b["follower_count"] > a["follower_count"]:
        winner = ("B", b)
    else:
        winner = ("D",)
    if choice == winner[0]:
        return True, winner[1]
    else:
        return False, None


higher_or_lower()
