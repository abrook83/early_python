from turtle import Turtle, Screen
import random
import time
from paddle import Paddle

screen  = Screen()
# paddle = Paddle()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)        # setting to '0' turns off animation while paddle is created...

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# paddle = Turtle("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.penup()
# paddle.goto(-350, 0)


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(-350, new_y)


# def go_dn():
#     new_y = paddle.ycor() - 20
#     paddle.goto(-350, new_y)


screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_dn)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_dn)

game_on = True

while game_on:
    screen.update()     # now paddle is created, updates screen to update animation


screen.exitonclick()