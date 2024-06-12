import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.group = []
        self.hideturtle()
        self.a=0


    def create_turtle(self):
        #create turtle
        C_turtle=Turtle()
        colour=COLORS[random.randint(0,5)]
        C_turtle.color(colour)
        C_turtle.shape("square")
        C_turtle.penup()
        C_turtle.shapesize(1,3)

        loca=random.randint(-250,250)
        C_turtle.setposition(280,loca)
        self.group.append(C_turtle)







    def move_car(self):
        print("trigger")

        for i in self.group:
             print("in loop")
        #     x=self.group[i].xcor()+MOVE_INCREMENT
        #     y=self.group[i].ycor()
        #     self.group[i].setposition(x,y)
        #     print(self.group[i])

