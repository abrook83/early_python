import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross That Road")
screen.tracer(0)        # this turns auto screen updating OFF, updating is set in the game's while loop with the timer.

player = Player()       # place this after the 'tracer' setting is turned off, so that the turtle appears at the bottom of the screen.

screen.listen()
screen.onkeypress(key="Up", fun=player.move)     # 'onkeypress' instead of 'onkey' works with key down....

game_is_on = True
while game_is_on:
    time.sleep(0.1)     # sets the code's delay, basically this code will run every 0.1 seconds.
    screen.update()




screen.exitonclick()