from turtle import Turtle



class Paddle:
    def __init__(self):
        self.h=1

    def create_paddle(self,n):
        self.paddle=Turtle(shape="square")
        self.paddle.penup()
        self.paddle.color("black")
        self.paddle.shapesize(5,1)
        self.paddle.goto(n,0)
    def move_up(self):
        new_y=self.paddle.ycor()+20
        self.paddle.goto(self.paddle.xcor(),new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)