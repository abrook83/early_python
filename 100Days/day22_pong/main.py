from turtle import Turtle, Screen
import random
import time
from paddle import Paddle
from ball import Ball

screen  = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)        # setting to '0' turns off animation while paddle is created...

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()      # need to pass in coordinates as one input argument, hence the double brackets

# print(ball.shapesize())

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_dn)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_dn)

game_on = True

while game_on:
    time.sleep(0.03)
    screen.update()     # now paddle is created, updates screen to update animation
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()


screen.exitonclick()