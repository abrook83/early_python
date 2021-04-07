from turtle import Turtle


class Ball(Turtle):

    def __init__ (self):
        """Creates the instance of the ball, ingeriting settings from the Turtle class."""
        super().__init__()
        self.shape("circle")
        self.speed("slowest")
        self.turtlesize(1,1)
        self.color("white")
        self.penup()
        self.x_move = 10        # variables to determine the ball's movin distance
        self.y_move = 10


    def move(self):
        """Runs in the main game's while loop: with every screen update, current coordinates will be read
        and added to to create a new 'goto'."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):
        """To bounce, will nultiply the y coord by -1 to make the ball turn 180deg the opposite direction."""
        self.y_move *= -1
