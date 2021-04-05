from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.screensize(600, 600)         # set screen size
screen.bgcolor("darkblue")
screen.title("Snaaaaaake!!!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
  
screen.exitonclick()