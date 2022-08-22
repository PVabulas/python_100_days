from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.color("white")
        self.write(f"Score: {self.score}", font=("Arial", 12, "normal"), align="Center")

    def increase_score(self):
        self.undo()
        self.score += 1
        self.write(f"Score: {self.score}", font=("Arial", 12, "normal"), align="Center")
