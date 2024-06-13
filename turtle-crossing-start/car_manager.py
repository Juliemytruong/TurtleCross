import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        colour=COLORS[random.randint(0,5)]
        self.color(colour)
        self.shape("square")
        self.penup()
        self.shapesize(1,3)
        self.setheading(180)


    def start_car(self):
        #create turtle

        loca=random.randint(-250,250)
        self.setposition(280,loca)




    def move_car(self):
        self.forward(MOVE_INCREMENT)
        print("trigger")


