import colorgram
import random
import turtle as t
from turtle import Turtle, Screen

colours = colorgram.extract(
    r"C:\Users\PVabulas\OneDrive\Github Repos - Personal\Udemy\Python - 100 Days\Day20 - Turtle Spot Painting\damien-hirst-spot-painting-for-sale.jpg",
    111,
)
rgb_colours = [colour.rgb for colour in colours if colour.proportion < 0.05]

t.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(2)
timmy.speed(0)


def set_random_colour(pen, mode="pen"):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    modes = {"pen": pen.pencolor, "fill": pen.fillcolor, "all": pen.color}
    modes[mode](red, green, blue)


def draw_polygon(pen, sides, length):
    ext_angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.right(ext_angle)


def random_walk(pen, num_steps, length, headings=[0, 90, 180, 270]):
    for _ in range(num_steps):
        pen.forward(length)
        pen.seth(random.choice(headings))
        set_random_colour(pen)


def spiro_circles(pen, num_circles, radius=100):
    turn_angle = 360 / num_circles
    for _ in range(num_circles):
        set_random_colour(pen, mode="all")
        pen.circle(radius)
        pen.right(turn_angle)


timmy.penup()
timmy.setpos(-342, -342)
for _ in range(10):
    for __ in range(10):
        timmy.pendown()
        timmy.color(random.choice(rgb_colours))
        timmy.begin_fill()
        timmy.circle(20, steps=500)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(70)
    timmy.right(180)
    timmy.forward(700)
    timmy.right(90)
    timmy.forward(70)
    timmy.right(90)

screen = Screen()
screen.exitonclick()

