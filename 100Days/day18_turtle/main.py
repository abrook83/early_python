import turtle as t
import tkinter
import random

tim = t.Turtle()
# screen = Screen()

t.colormode(255)

def random_colour():
    """Generates a tuple to plug into the r,g,b space."""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


tim.shape('turtle')
tim.color(random_colour())
tim.speed(0)
tim.width(15)
t.screensize(400, 400)

# pen_colours = [
#     "aquamarine",
#     "dodger blue",
#     "orange red",
#     "dark magenta",
#     "gold",
#     "deep pink",
#     "cyan",
# ]

# def draw_shape(no_of_sides):
#     """draws the shape depending on the number of sides input."""
#     angle = 360 / no_of_sides
#     for _ in range(no_of_sides):
#         tim.fd(100)
#         tim.rt(angle)
    
# for no_of_sides in range(3, 15):
#     tim.pencolor(random.choice(pen_colours))
#     draw_shape(no_of_sides)


angles = [0, 90, 180, 270]

def random_walk(no_of_steps):
    """draws a random walk depending on the number of steps input."""
    for _ in range(no_of_steps):
        angle = random.choice(angles)
        # dist = random.choice(range(20, 100))
        tim.fd(30)
        tim.setheading(angle)
        tim.pencolor(random_colour())
    
    
random_walk(200)


def spirograph():
    pass

# screen = Screen()
# screen.exitonclick()
