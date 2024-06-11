import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)



Crosser=Player()
Crosser.start()

screen.onkey(Crosser.move,"Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()








