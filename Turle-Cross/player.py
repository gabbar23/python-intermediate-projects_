from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)


    def start(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor()==220:
            return True
        else:
            return False
