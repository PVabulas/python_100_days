from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, size=20):
        super().__init__()
        self.size = size
        self.shape("circle")
        self.penup()
        self.shapesize(0.5 * size / 20, 0.5 * size / 20)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = (
            randint(-int(14 * 20 / self.size), int(14 * 20 / self.size)) * self.size
        )
        random_y = (
            randint(-int(14 * 20 / self.size), int(13 * 20 / self.size)) * self.size
        )
        self.goto(random_x, random_y)
