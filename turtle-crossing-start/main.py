import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

car_group=[]

Crosser=Player()
Crosser.start()

screen.onkey(Crosser.move,"Up")

score=Scoreboard()

game_is_on = True
while game_is_on:

    carA = CarManager()
    carA.start_car()
    car_group.append(carA)
    #print(car_group)
    for i in range (4):
        time.sleep(0.1)
        screen.update()

        for i in car_group:
            x=i.xcor()+10
            y=i.ycor()
            #print(x,y)
            i.move_car()

        for i in car_group:
            pos=i.position()
            print(pos)
            if Crosser.distance(pos)<20:
                Crosser.setposition(0, -280)

        if Crosser.ycor()>280:
            score.add_score()
            Crosser.setposition(0,-280)























