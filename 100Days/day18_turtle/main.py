# import colorgram

# rgb_colours = []
# # use colorgram to extract the most frequent colours from the input image, number indicates how many....
# colours = colorgram.extract('100Days\day18_turtle\image.jpg', 30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r,g,b)
#     # then add each extracted colour to the list as an rgb...
#     rgb_colours.append(new_colour)

# print(rgb_colours)

import turtle as t
import random

colour_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
(170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
(232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
(147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

tim = t.Turtle()
t.colormode(255)

tim.speed(0)

def create_art(width, height):
    for nheight in range(height):
        for nwidth in range(width - 1):
            tim.dot(25, random.choice(colour_list))
            tim.fd(70)
        tim.dot(25, random.choice(colour_list))
        if tim.xcor() < 0:
            tim.rt(90)
            tim.fd(70)
            tim.rt(90)
        else:
            tim.lt(90)
            tim.fd(70)
            tim.lt(90)  


tim.penup()
tim.hideturtle()
tim.setpos(-315,-315)
create_art(10,10)
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()