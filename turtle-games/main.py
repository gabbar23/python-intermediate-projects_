# This is a sample Python script.
from turtle import Turtle, Screen
import random

game_end = False
screen = Screen()
screen.setup(500, 500)
user_bet = screen.textinput(title='Make Your bet', prompt='On which turtle you want to make bet on?')
color = ["purple", "red", "black", "yellow", "pink"]
y = [100, 50, 0, -50, -100]
y2 = [-100, -50, 0, 50, 100]
y_axis = []

line = Turtle()
line.penup()
line.goto(x=220, y=-110)
line.setheading(90)
line.dot(5, 'black')
for i in range(0, 11):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.penup()
    turtle_color = color[i]
    tim.color(turtle_color)
    tim.goto(x=-220, y=y[i])
    y_axis.append(tim)

if user_bet:
    game_end = True

while game_end:

    for turtle in y_axis:
        if turtle.xcor() > 210:
            game_end = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won your bet on {winning_color}")
            else:
                print(f"You Lost! {winning_color} Won!")

        turtle.forward(random.randint(1, 10))

#

screen.exitonclick()
