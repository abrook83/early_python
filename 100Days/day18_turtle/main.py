from turtle import Turtle, Screen, pendown, penup
import tkinter
import random

tim = Turtle()

tim.shape('turtle')
tim.color('green4')

pen_colours = [
    "aquamarine",
    "dark goldenrod",
    "dodger blue",
    "orange red",
    "dark magenta",
    "gold",
    "deep pink",
    "cyan",
]

def draw_shape(no_of_sides):
    """draws the shape depending on the number of sides input."""
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        tim.fd(100)
        tim.rt(angle)
    

for no_of_sides in range(3, 11):
    tim.pencolor(random.choice(pen_colours))
    draw_shape(no_of_sides)


# for dash in range(15):
#     tim.pd()
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)






screen = Screen()
screen.exitonclick()
