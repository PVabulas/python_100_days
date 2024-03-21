import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "Day25 - US States/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("Day25 - US States/50_states.csv")
remaining_states = list(states.state)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")

correct = 0
while True:
    try:
        answer= screen.textinput(title = f"{correct}/50 correct", prompt="What's another state's name?").title()
    except AttributeError:
        break
    if answer in remaining_states:
        line = states[states.state == answer]
        writer.goto(int(line.x.iloc[0]), int(line.y.iloc[0]))
        writer.write(f"{answer}", align="center", font=("Courier", 88, "normal"))
        remaining_states.remove(answer)
        correct += 1
        if correct == 50:
            break
    else:
        print(f"Can't find {answer}")

with open("Day25 - US States/remaining_states.txt", "w") as f:
    f.write(", ".join(remaining_states))
screen.exitonclick()