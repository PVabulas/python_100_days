from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
START_LIVES = 3


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        # self.color("black")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)
        self.lives = START_LIVES

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return 1
        else:
            return 0
            
    def lose_life(self):
        self.lives -= 1
        self.goto(STARTING_POSITION)
