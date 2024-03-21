from turtle import Turtle, textinput
from time import sleep

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard(None)

    def update_scoreboard(self, lives):
        self.clear()
        self.goto(-280, 240)
        self.write(f"Level: {self.level}\nLives: {lives}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)

        