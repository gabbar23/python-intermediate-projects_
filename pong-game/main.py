from turtle import Turtle,Screen
from paddle import Paddle
START_CORD1=((-340,0),(-340,20),(-340,40))
START_CORD2=((340,0),(340,20),(340,40))

screen=Screen()
screen.bgcolor("white")
screen.setup(700,500)
screen.tracer(0)
paddle=Paddle()
paddle1=Paddle()
paddle.create_paddle(330)
paddle1.create_paddle(-332)
screen.listen()
screen.onkeypress(paddle.move_up,'Up')
screen.onkeypress(paddle.move_down,'Down')
screen.onkeypress(paddle1.move_up,'w')
screen.onkeypress(paddle1.move_down,'s')


while True:
    screen.update()
























screen.exitonclick()