from turtle import Turtle


class Ball(Turtle):

    def __init__ (self):
        """Creates the instance of the ball, inheriting settings from the Turtle class."""
        super().__init__()
        self.shape("circle")
        self.speed("slowest")
        self.turtlesize(1,1)
        self.color("white")
        self.penup()
        self.x_move = 10        # variables to determine the ball's movin distance
        self.y_move = 10
        self.move_speed = 0.07


    def move(self):
        """Runs in the main game's while loop: with every screen update, current coordinates will be read
        and added to to create a new 'goto'."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):
        """To bounce off the walls, will multiply the y coord by -1 to make the ball bounce in the opposite direction."""
        self.y_move *= -1


    def paddle_hit(self):
        """To bounce off the paddle, will multiply the x coord by -1 to make the ball bounce in the opposite direction.
        Also increases the ball's speed with every paddle hit. """
        self.x_move *= -1
        self.move_speed *= 0.95


    def reset_position(self):
        """Reset the ball once it's goe out of bounds - resets the original speed, places the ball
        in the middle, and sends it the opposite way it has heading."""
        self.move_speed = 0.1
        self.goto(0,0)
        self.paddle_hit()