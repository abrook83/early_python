import time
from random import uniform
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross That Road")
screen.tracer(0)        # this turns auto screen updating OFF, updating is set in the game's while loop with the timer.

player = Player()       # place this after the 'tracer' setting is turned off, so that the turtle appears at the bottom of the screen.
scores = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)     # 'onkeypress' instead of 'onkey' works with key down....

game_on = True

while game_on:
    time.sleep(0.1)     # sets the code's delay, basically this code will run every 0.1 seconds.
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scores.game_over()
            game_on = False

    # reset the player when they reach the top, increment score
    if player.ycor() > 280:
        scores.update_score()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()