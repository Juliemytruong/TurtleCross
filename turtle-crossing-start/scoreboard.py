from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(-280, 250)
        self.write(f"score is {self.score}", True, "left", (FONT))

    def add_score(self):
        self.score+=1
        self.clear()
        self.write(f"score is {self.score}", True, "left", (FONT))


