from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color('white')
        self.speed("fastest")
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 15, "normal"))

    def score_add(self):
        self.score+= 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("G A M E   O V E R", move=False, align="center", font=("Arial", 15, "normal"))


