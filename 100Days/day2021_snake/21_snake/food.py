from turtle import Turtle
import random


class Food(Turtle):     # passes the Turtle class into the Food class
    """Inherits all attributes from the Turtle class to be used in the Food class."""
    def __init__(self):
        super().__init__()      # call the 'init' method from the super class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # 'stretches' the size of the circle shape to half its original
        self.color("orange")
        self.speed("fastest")
        self.refresh_food


    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)