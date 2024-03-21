import turtle as t
from turtle import Screen, Turtle

from snake import Snake
from food import Food
from scoreboard import Scoreboard


def run_game():
    speed_dict = {"fast": 0.05, "normal": 0.1, "slow": 0.2}

    t.colormode(255)
    screen = Screen()
    screen_width = 600
    screen_height = 600
    screen.setup(width=screen_width, height=screen_height)
    screen.bgcolor("black")
    screen.title("Snake")
    speed = speed_dict[
        screen.textinput("Select game speed", "Fast, Normal, or Slow?").lower()
    ]
    screen.tracer(n=0)
    screen.listen()

    snake = Snake(screen, size=20, speed=speed)
    food = Food(snake.size)
    score = Scoreboard()
    screen.update()

    is_game_on = True
    while is_game_on:
        snake.move()
        if snake.head.distance(food) < 5:
            food.refresh()
            score.increase_score()
            snake.add_body()
        if snake.detect_collision(screen_width, screen_height):
            is_game_on = False

    game_over = Turtle(visible=False)
    game_over.color("white")
    game_over.write("Game Over", align="center", font=("Courier", 24, "normal"))
    screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    run_game()
