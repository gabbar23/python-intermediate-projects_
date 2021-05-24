from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cord=10
        self.y_cord=10
        self.fast=.1
    def move(self):
        new_y=self.ycor()+self.y_cord
        new_x=self.xcor()+self.x_cord
        self.goto(new_x,new_y)


    def bounce(self):
        self.y_cord *=-1


    def paddle_bounce(self):
        self.x_cord *=-1
        self.fast *= .9

    def reset(self):
        self.goto(0,0)
        self.fast=.1
        randomly=random.choice([-1,1,-1,1,-1,1])
        if randomly==1:
            self.x_cord *= 1
        if randomly==-1:
            self.x_cord *= -1
