from turtle import Turtle


class Paddle(Turtle):

    def __init__ (self, start_pos):
        """Creates a paddle, taking input coordinates to determine where. Inherits attributes from the Turtle class."""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(start_pos)


    def go_up(self):
        """Both 'go_up' & 'go_dn' move the paddle when told to (input from keyboard in 'main'."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_dn(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

