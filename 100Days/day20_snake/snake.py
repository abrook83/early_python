from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

class Snake:
    def __init__ (self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle("square")
            snake_segment.color("yellow")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):        # '-1' steps through in reverse
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DIST)