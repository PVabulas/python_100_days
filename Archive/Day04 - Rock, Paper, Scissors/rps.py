rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

rps = [rock, paper, scissors]
player_choice = rps[
    int(
        input(
            "What is your choice? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"
        )
    )
]
comp_choice = random.choice(rps)
print(player_choice)
print("Computer chose:")
print(comp_choice)
win_options = {
    (rock, rock): "You draw",
    (rock, paper): "You lose",
    (rock, scissors): "You win!",
    (paper, paper): "You draw",
    (paper, scissors): "You lose",
    (paper, rock): "You win!",
    (scissors, scissors): "You draw",
    (scissors, rock): "You lose",
    (scissors, paper): "You win!",
}
print(win_options[(player_choice, comp_choice)])
