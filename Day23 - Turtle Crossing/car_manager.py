from turtle import Turtle
from random import choice, randrange, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
MAX_CARS = 15


class CarManager():
    def __init__(self):
        self.cars = []
        
    def create_car(self):
        self.cars.append(Car())
        
    def add_rand_car(self):
        if len(self.cars) < MAX_CARS and randint(1, MAX_CARS) == MAX_CARS:
            self.create_car()

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -320 and randint(1,4) == 4:
                car.reset_car()
        self.add_rand_car()

    def update_speed(self, level):
        for car in self.cars:
            car.move_dist = STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level-1)

    def detect_collisions(self, xcor, ycor):
        for car in self.cars:
            if abs(xcor-car.xcor()) <= 30 and abs(ycor-car.ycor()) <= 15:
                return True
        return False


    
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.move_dist = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.seth(180)
        self.reset_car()

    def reset_car(self):
        self.color(choice(COLORS))
        start_y = randint(-200, 200)
        self.goto(280, start_y)
        
    def move(self):
        self.forward(self.move_dist)
        