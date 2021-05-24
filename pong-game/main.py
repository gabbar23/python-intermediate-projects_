from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time


START_CORD1 = ((-340, 0), (-340, 20), (-340, 40))
START_CORD2 = ((340, 0), (340, 20), (340, 40))

ball = Ball()
score_l=Scoreboard((-50,220))
score_r=Scoreboard((50,220))
screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(700, 500)
screen.tracer(0)
r_paddle = Paddle((330, 0))
l_paddle = Paddle((-330, 0))
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

while True:
    screen.update()
    time.sleep(ball.fast)
    ball.move()

    if ball.ycor() > 235 or ball.ycor() < -235:
        ball.bounce()

    if (ball.distance(l_paddle) < 50 and ball.xcor() < -310) or (ball.distance(r_paddle) < 50 and ball.xcor() > 310):
        ball.paddle_bounce()

    if ball.xcor()>360:
        score_l.score_add()
        ball.reset()

    if ball.xcor() < -360:
        score_r.score_add()
        ball.reset()

