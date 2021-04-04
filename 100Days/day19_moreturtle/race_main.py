from turtle import Turtle, Screen, color
import turtle
import random

screen = Screen()
screen.setup(width=1000, height=400)     # screen size settings

user_bet = turtle.textinput('Make your bet', 'Which turtle will win the race?')
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -((len(colours) / 2) *40)

print(user_bet)

for colour in colours:
    racer = Turtle(shape="turtle")
    racer.color(colour)
    racer.penup()
    racer.goto(-450,y)
    y += 40









screen.exitonclick()