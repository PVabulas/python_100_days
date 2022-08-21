import turtle as t

tim = t.Turtle()
screen = t.Screen()


def forward():
    tim.forward(1)


def backward():
    tim.backward(1)


def right():
    tim.right(1)


def left():
    tim.left(1)


def clear():
    tim.reset()


screen.listen()
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="c", fun=clear)
screen.onkeypress(key="w", fun=forward)

screen.exitonclick()
