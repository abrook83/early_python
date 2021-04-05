from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.screensize(600, 600)         # set screen size
screen.bgcolor("darkblue")
screen.title("Snaaaaaake!!!")
screen.tracer(0)

start_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in start_positions:
    snake_segment = Turtle("square")
    snake_segment.color("yellow")
    snake_segment.penup()
    snake_segment.goto(position)
    segments.append(snake_segment)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for segment_number in range(len(segments) - 1, 0, 1):        # '-1' steps through in reverse
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number - 1].ycor()
        segments[segment_number].goto(new_x, new_y)
    segments[0].fd(20)
    

screen.exitonclick()