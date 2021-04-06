from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)         # set screen size
screen.bgcolor("darkblue")
screen.title("Snaaaaaake!!!")
screen.tracer(0)        # setting tracer to 0 turns live turtle animations off, so the screen can be updated as determined

snake = Snake()         # refer to the Snake classes from snake
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()        # as tracer is off, screen is updated within this function, with below delay of 0.1 seconds added.
    time.sleep(0.1)
    snake.move()            # run the move function from the snake variable, whish is from the Snake class

    # detect collision between snake & food
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        score.update_score()
        snake.extend()

    # detect a collision with a wall
    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -300:
        game_on = False
        score.game_over()

    # detect a collision with the snake's tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()