from turtle import  Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().penup()
        super().color("red")
        super().shapesize(.8)
        super().speed("fastest")
        self.draw()

    def draw(self):
        new_x=random.randint(-300,300)
        new_y= random.randint(-250, 250)
        super().goto(x=new_x,y=new_y)



