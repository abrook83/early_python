from turtle import Turtle, Screen, screensize

tim = Turtle()
screen = Screen()

def move_fwd():
    tim.fd(10)

screen.listen()
screen.onkey(key='space', fun=move_fwd)
screen.exitonclick()
