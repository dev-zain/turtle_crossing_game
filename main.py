import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Create a turtle
player = Player()
screen.listen()
screen.onkey(player.move_forward, 'Up')

#Scoreboard
scoreboard = Scoreboard()


#Create cars
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create and move cars
    car.create_car()
    car.move_car()

    #detect collision with car
    for i in car.all_cars:
        if player.distance(i)<20:
            scoreboard.game_over()
            game_is_on = False

    #check if turtle reached at finish line
    if player.is_at_finih_line():
        player.starting_position()
        scoreboard.next_level()
        car.level_up()

screen.exitonclick()

    
