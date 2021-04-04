from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fwd():
    tim.fd(10)

def move_bk():
    tim.bk(10)

def turn_l():
    tim.rt(10)

def turn_r():
    tim.lt(10)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_fwd)     # arguments cannot receive a function with another argument (eg. "tim.fd(10)"),
screen.onkey(key="s", fun=move_bk)      # so must create our own instance of the function, then plug
screen.onkey(key="a", fun=turn_l)       # that in as an argument.
screen.onkey(key="d", fun=turn_r)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
