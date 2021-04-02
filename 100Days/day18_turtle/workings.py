import turtle as t
import tkinter
import random

tim = t.Turtle()

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
tim.width(1)
t.screensize(400, 400)


def draw_shape(no_of_sides):
    """draws the shape depending on the number of sides input."""
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        tim.fd(100)
        tim.rt(angle)
    

angles = [0, 90, 180, 270]

def random_walk(no_of_steps):
    """draws a random walk depending on the number of steps input."""
    for _ in range(no_of_steps):
        angle = random.choice(angles)
        # dist = random.choice(range(20, 100))
        tim.fd(30)
        tim.setheading(angle)
        tim.pencolor(random_colour())


def spirograph(loops):
    """Draw a spirograph-like circle."""
    for _ in range(loops):
        tim.circle(150)
        tim.lt(360 / loops)
        tim.pencolor(random_colour())


# ### run the spirograph -
# spirograph(100)       # pass in the number of loops

# ### run the shape generator -
# for no_of_sides in range(3, 15):      # pass in the min & max no. of sides
#     tim.color(random_colour())
#     draw_shape(no_of_sides)

### run the random walk -
random_walk(200)        # pass in the number of steps


screen = t.Screen()
screen.exitonclick()
