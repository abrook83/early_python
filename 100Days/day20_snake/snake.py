from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__ (self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]


    def create_snake(self):
        """Creates the snake out of 3 squares in the positions listed in STARTING_POSITIONS."""
        for position in STARTING_POSITIONS:
            snake_segment = Turtle("square")
            snake_segment.color("yellow")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)


    def move(self):
        """Moves the snake, though to limit screen flutter, snake moves from last to first square.
        For each segment number from last to first, we step through and create new x & y coordinates
        by reading the coordinates of the next square in the list. These new coordinates then 
        are passed to the current block to update itself."""
        for segment_number in range(len(self.segments) - 1, 0, -1):        # '-1' steps through in reverse
            new_x = self.segments[segment_number - 1].xcor()            # takes the next in line square's coordinates....
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)            # plugs those acquired coordinates into the current square
        self.snake_head.fd(MOVE_DIST)          # lastly, move the first square forward to begin the process again.


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)


    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)


    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)


    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)