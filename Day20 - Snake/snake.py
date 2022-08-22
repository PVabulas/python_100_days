from turtle import Turtle
from time import sleep


class Snake:
    def __init__(self, screen, length=3, size=20, speed=0.1):
        screen.onkey(self.turn_left, "Left")
        screen.onkey(self.turn_right, "Right")
        self.screen = screen
        self.size = size
        self.speed = speed
        self.create_snake(length)
        self.head = self.snake[0]

    def create_snake(self, length):
        snake = [Turtle("square") for _ in range(length)]
        for i, body in enumerate(snake):
            body.resizemode("user")
            body.shapesize(self.size / 20, self.size / 20)
            body.penup()
            body.color("white")
            body.goto(-self.size * i, 0)
            body.speed("fastest")
        self.snake = snake

    def turn_left(self):
        self.head.left(90)

    def turn_right(self):
        self.head.right(90)

    def move(self):
        for body in self.snake:
            if body is self.head:
                next_coord = body.pos()
                body.forward(self.size)
            else:
                holding_coord = body.pos()
                body.goto(next_coord)
                next_coord = holding_coord
        sleep(self.speed)
        self.screen.update()
        return next_coord

    def add_body(self):
        position = self.move()
        body = Turtle("square")
        body.resizemode("user")
        body.shapesize(self.size / 20, self.size / 20)
        body.penup()
        body.color("white")
        body.speed("fastest")
        body.goto(position)
        self.snake.append(body)

    def detect_collision(self, screen_width, screen_height):
        if (self.head.xcor() <= -int(screen_width / 2)) | (
            self.head.xcor() >= int(screen_width / 2)
        ):
            print("X_collision")
            return True
        if (self.head.ycor() <= -int(screen_height / 2)) | (
            self.head.ycor() >= int(screen_height / 2)
        ):
            print("Y_collision")
            return True
        for body in self.snake[1:]:
            if self.head.distance(body) <= 5:
                print(f"body_collision, {self.snake.index(body)}")
                return True
        return False
