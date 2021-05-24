from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, n):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(n)

    def move_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)