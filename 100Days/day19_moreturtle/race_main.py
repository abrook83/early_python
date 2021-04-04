from turtle import Turtle, Screen
import turtle

tim = Turtle()
screen = Screen()
screen.setup(width=1000, height=800)     # screen size settings

user_bet = turtle.textinput('Make your bet', 'Which turtle will win the race?')
print(user_bet)









screen.exitonclick()