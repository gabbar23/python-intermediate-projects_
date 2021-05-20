from turtle import Turtle
STARTING_CORD=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake():
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.head=self.snake_body[0]

    def create_snake(self):
        for position in STARTING_CORD:
            snake=Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    def move_forward(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        else:
            pass

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

    def move_right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
        else:
            pass

    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)