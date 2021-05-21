from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

turtle=Turtle()
screen=Screen()
screen.setup(width=700,height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.move_up,'Up')
screen.onkey(snake.move_down,'Down')
screen.onkey(snake.move_left,'Left')
screen.onkey(snake.move_right,'Right')


game_end=True
while game_end:
    screen.update()
    time.sleep(.09)
    snake.move_forward()
    if snake.head.distance(food)<20:
        food.draw()
        score.score_add()
        snake.add_snake()

    if snake.head.xcor()>340 or snake.head.xcor()< -340 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        game_end=False
        score.game_over()

    for segment in snake.snake_body[1:]:
       if snake.head.distance(segment)<10:
          game_end=False
          score.game_over()


screen.exitonclick()