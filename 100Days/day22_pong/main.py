from turtle import Turtle, Screen
import random
import time
from paddle import Paddle
from ball import Ball
from scores import Scores

screen  = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)        # setting to '0' turns off animation while paddle is created...

l_paddle = Paddle((-350, 0))        # need to pass in coordinates as one input argument, hence the double brackets
r_paddle = Paddle((350, 0))
ball = Ball()
scores = Scores()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.go_up)     # 'onkeypress' instead of 'onkey' works with key down....
screen.onkeypress(key="Down", fun=r_paddle.go_dn)
screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_dn)

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()     # now paddle is created, updates screen to update animation
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect a collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.paddle_hit()

    # detect when the ball passes paddle and then resets to the centre
    if ball.xcor() > 380:
        scores.update_l_score()
        ball.reset_position()

    if ball.xcor() < -380:
        scores.update_r_score()
        ball.reset_position()

screen.exitonclick()