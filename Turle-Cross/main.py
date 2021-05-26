import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
player = Player()
cars=CarManager()
score=Scoreboard()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.onkeypress(player.move, "w")


# screen.onkeypress(player.right, "d")
# screen.onkeypress(player.left, "a")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.cars_move()

    for car in cars.cars_list:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()

    if player.at_finish_line():
        score.score_add()
        player.start()
        cars.car_speed_increase()


screen.exitonclick()
