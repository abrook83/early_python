from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__ (self):
        """Creates a turtle, taking input coordinates to determine where. Inherits attributes from the Turtle class."""
        super().__init__()
        self.shape("turtle")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("green")
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def move(self):
        """Move the turtle when told to (input from keyboard in 'main')."""
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

