from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    
    def __init__ (self):
        """Creates a turtle, taking input coordinates to determine where. Inherits attributes from the Turtle class."""
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.seth(90)
        self.penup()
        self.reset_position()


    def move(self):
        """Move the turtle when told to (input from keyboard in 'main')."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def reset_position(self):
        """Reset the turtle once it's reached the top of screen - resets the original speed, places the ball
        in the middle, and sends it the opposite way it has heading."""
        self.goto(STARTING_POSITION)

