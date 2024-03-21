# Screen
# Net
# Paddle(s)
# Ball
# Scoreboard(s)

import logging
from math import sqrt
import turtle as t
from turtle import Screen, Turtle
from time import sleep
from tkinter import TclError
from random import randint, choice

logging.basicConfig(level=logging.CRITICAL, format="%(asctime)s - %(levelname)s - %(message)s")

def run_game():
    speed_dict = {"fast": 0.05, "normal": 0.1, "slow": 0.2}

    t.colormode(255)
    screen = Screen()
    screen_width = 1200
    screen_height = 600
    screen.setup(width=screen_width, height=screen_height)
    screen.bgcolor("black")
    screen.title("Pong")
    #    speed = speed_dict[
    #        screen.textinput("Select game speed", "Fast, Normal, or Slow?").lower()
    #    ]
    screen.tracer(n=0)
    screen.listen()

    game = Game(screen_width, screen_height)
    screen.onkey(game.left_paddle.move_up, "w")
    screen.onkey(game.left_paddle.move_down, "s")
    screen.onkey(game.right_paddle.move_up, "Up")
    screen.onkey(game.right_paddle.move_down, "Down")
    screen.onkey(game.quit_game, key="q")

    try:
        while game.game_is_on:
            screen.update()
            game.move()
        screen.exitonclick()
    except TclError:
        print("Game closed")

class Game:
    game_is_on = True

    def __init__(self, screen_width, screen_height) -> None:
        logging.debug(f"scr_height:{screen_height}; scr_width:{screen_width}")
        self.scr_wdth = screen_width
        self.scr_hght = screen_height
        Net(screen_height)
        self.left_paddle = Paddle(screen_width, "left")
        self.right_paddle = Paddle(screen_width, "right")
        self.ball = Ball(screen_width, screen_height, self.left_paddle, self.right_paddle)
        self.left_score = Scoreboard(screen_height, "left")
        self.right_score = Scoreboard(screen_height, "right")

    def move(self):
        outcome, xcor = self.ball.move_ball()
        if outcome == "goal":
            if xcor < 0:
                self.right_score.increase_score()
            else:
                self.left_score.increase_score()
        if self.left_score.score == 5:
            print("Player 1 wins")
            self.game_is_on = False
        if self.right_score.score == 5:
            print("Player 2 wins")
            self.game_is_on = False

    def quit_game(self):
        self.game_is_on = False
        print("Game is off")


class Net(Turtle):
    def __init__(self, screen_height) -> None:
        super().__init__(visible=False)
        self.penup()
        self.goto(5, int(screen_height / 2))
        self.setheading(270)
        self.color("white")
        for i in range(int(screen_height / 50)):
            self.pendown()
            self.begin_fill()
            self.forward(25)
            self.right(90)
            self.forward(10)
            self.right(90)
            self.forward(25)
            self.right(90)
            self.forward(10)
            self.right(90)
            self.end_fill()
            self.penup()
            self.forward(50)


class Paddle:
    def __init__(self, screen_width, side):
        if side == "left":
            x_pos = -(int(screen_width / 2) - 20)
        elif side == "right":
            x_pos = int(screen_width / 2) - 20
        else:
            raise AttributeError("side must be 'left' or 'right'")

        self.paddle = [Turtle("square") for _ in range(5)]
        for i, part in enumerate(self.paddle):
            part.penup()
            part.color("white")
            y_pos = -40 + i * 20
            part.goto(x_pos, y_pos)

    def move_up(self):
        for part in self.paddle:
            part.setheading(90)
            part.forward(20)

    def move_down(self):
        for part in self.paddle:
            part.setheading(270)
            part.forward(20)


class Ball(Turtle):
    def __init__(self, screen_width, screen_height, left_paddle, right_paddle) -> None:
        super().__init__("square")
        self.scr_wdth = screen_width
        self.scr_hght = screen_height
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
        self.penup()
        self.color("white")
        self.goto(-int(screen_width / 2) + 40, 0)
        self.seth(randint(15,75)*choice([1,-1]))

    def replace(self, side):
        side = -1 if side == "left" else 1
        self.goto(side*int(self.scr_wdth / 2) + (-side)*40, self.ycor())
        self.seth((90+randint(15,75)*side)*choice([1,-1]))


    def move_ball(self):
        self.forward(sqrt(2*20**2))
        if self.detect_top_bot_collision():
            self.seth(-self.heading())
        if self.detect_goal():
            if self.xcor() < 0:
                self.replace("left")
            else:
                self.replace("right")
            return "goal", self.xcor()
        hit_paddle = self.detect_paddle()
        if hit_paddle == "left":
            self.replace("left")
        elif hit_paddle == "right":
            self.replace("right")
        sleep(0.1)
        return "no goal", 0

    def detect_top_bot_collision(self):
        if abs(self.ycor()) > self.scr_hght/2 - 40:
            return True
        
    def detect_goal(self):
        if abs(self.xcor()) > self.scr_wdth/2+40:
            return True

    def detect_paddle(self):
        # logging.debug(f"{self.left_paddle[0]}")
        left_paddle_y_cors = [section.ycor() for section in self.left_paddle.paddle]
        right_paddle_y_cors = [section.ycor() for section in self.right_paddle.paddle]
        if self.xcor() <= -self.scr_wdth/2+40:
            for cor in left_paddle_y_cors:
                if abs(self.ycor() - cor) <= 5:
                    return "left"
        if self.xcor() >= self.scr_wdth/2-40:
            for cor in right_paddle_y_cors:
                if abs(self.ycor() - cor) <= 5:
                    return"right"
                

class Scoreboard(Turtle):
    def __init__(self, screen_height, side) -> None:
        super().__init__(visible=False)
        self.color("white")
        self.score = 0
        self.penup()
        if side == "left":
            x_pos = -100
            self.align = "Right"
        elif side == "right":
            x_pos = 100
            self.align = "Left"
        else:
            raise AttributeError("side must be 'left' or 'right'")
        y_pos = int(screen_height / 2) - 150
        self.goto(x_pos, y_pos)
        self.pendown()
        self.write(f"{self.score}", font=("Bit5x3", 100, "normal"), align=self.align)

    def increase_score(self):
        self.undo()
        self.score += 1
        self.write(f"{self.score}", font=("Bit5x3", 100, "normal"), align=self.align)


if __name__ == "__main__":
    run_game()
