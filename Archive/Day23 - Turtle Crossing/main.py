from time import sleep
from turtle import Screen, Terminator
from player import Player, START_LIVES
from car_manager import CarManager
from scoreboard import Scoreboard
from tkinter import TclError

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
cars = CarManager()

def move_player():
    scoreboard.level += player.move()
    scoreboard.update_scoreboard(player.lives)

def restart():
    player.lives = 3
    scoreboard.level = 1

game_is_on = True

screen.listen()
screen.onkey(move_player, "Up")
screen.onkey(restart, "r")

try:
    while game_is_on:
        sleep(0.1)
        cars.move_cars()
        if cars.detect_collisions(player.xcor(), player.ycor()):
            player.lose_life()
        if player.lives <= 0:
            scoreboard.game_over()
            screen.update()
            sleep(3)
            restart()
        cars.update_speed(scoreboard.level)
        screen.update()
    screen.exitonclick()
except TclError:
    pass
except Terminator:
    pass
print("Game closed")