from turtle import Turtle


class Ball(Turtle):

    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.speed("slowest")
        self.turtlesize(1,1)
        self.color("white")
        self.penup()


    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)


    def wall_collision(self):
        new_heading = -(self.heading())
        y_coord = self.ycor()
        if y_coord > 300 or y_coord < -300:
            self.heading(new_heading)