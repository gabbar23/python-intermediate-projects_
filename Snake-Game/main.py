from turtle import Turtle,Screen
import time
from snake import Snake


screen=Screen()
screen.setup(width=700,height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
snake=Snake()

screen.listen()
screen.onkey(snake.move_up,'Up')
screen.onkey(snake.move_down,'Down')
screen.onkey(snake.move_left,'Left')
screen.onkey(snake.move_right,'Right')


game_end=True
while game_end:
    screen.update()
    time.sleep(.1)
    snake.move_forward()



# screen.listen()
# screen.onkey(fun=snake_body,key="space")



















screen.exitonclick()