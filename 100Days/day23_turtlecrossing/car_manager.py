from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

    def __init__ (self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

        
    def create_car(self):
        """Creates the cars at random, inheriting settings from the Turtle class."""
        random_choice = random.randint(1,6)     # every iteration generates a random number....
        if random_choice == 1:                  # if it's a one, then the loop continues...
            new_car  = Turtle("square")
            new_car.penup()
            car_y = random.randint(-250, 270)  # determine where on the y axis to create the car
            new_car.goto(320, car_y)              # place the car in the random y, at x = -300
            new_car.shapesize(stretch_wid=1, stretch_len=2)    # turtles are by default 20*20 pixels
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)


    def move_cars(self):
        """Runs in the main game's while loop: with every screen update, current x coordinate will be read
        and added to to create a new 'goto'."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

