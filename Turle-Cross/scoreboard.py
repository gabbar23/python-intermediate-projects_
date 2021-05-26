from turtle import  Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color('white')
        self.speed("fastest")
        self.goto(0,260)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def score_add(self):
        self.score+= 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"G A M E   O V E R", move=False, align="center", font=FONT)

