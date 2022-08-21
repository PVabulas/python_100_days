from random import randint
import turtle as t

t.colormode(255)

race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
response = screen.textinput("Place your bet", "Who's gonna win?")


def place_turtle(pen, x_coord, y_coord):
    pen.penup()
    pen.goto(x_coord, y_coord)
    pen.pendown()


turtles = [t.Turtle("turtle") for _ in range(6)]
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(6):
    turtle = turtles[i]
    turtle.color(colours[i])
    y_coord = -125 + 50 * i
    place_turtle(turtle, -230, y_coord)

race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 230:
            winner = turtle.color()[0]
            race_on = False

if response == winner:
    print("Congratulations! You won!")
else:
    print(f"Sadly {winner} won, you lose.")

screen.exitonclick()
