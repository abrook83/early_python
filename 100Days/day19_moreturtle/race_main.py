from turtle import Turtle, Screen, color
import turtle
import random

screen = Screen()
screen.setup(width=1000, height=400)     # screen size settings

race_on = False
user_bet = turtle.textinput('Make your bet', 'Which turtle will win the race?')
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -((len(colours) / 2) *40)
racer_list = []

for colour in colours:
    racer = Turtle(shape="turtle")
    racer.speed(0)
    racer.color(colour)
    racer.penup()
    racer.goto(-450,y)
    y += 40
    racer_list.append(racer)

if user_bet:
    race_on = True

while race_on:
    for racer in racer_list:
        if racer.xcor() > 450:
            race_on = False
            winning_colour = racer.pencolor()          
            if winning_colour == user_bet:
                print(f"{winning_colour.title()} wins, and so do you!")
            else:
                print(f"Sorry, you lost.... {winning_colour.title()} won the race!")    
        racer.fd(random.randint(0, 10))


screen.exitonclick()