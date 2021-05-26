from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars_list=[]
        self.car_speed=STARTING_MOVE_DISTANCE


    def create_car(self):
        random_var=random.randint(1,5)
        if random_var == 1:
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(.5, 2)
            car.color(random.choice(COLORS))
            ycord = random.randint(-300,250)
            car.goto(300,ycord)
            self.cars_list.append(car)


    def cars_move(self):
        for i in self.cars_list:
            i.backward(self.car_speed)


    def car_speed_increase(self):
        for car in self.cars_list:
            car.reset()
            car.hideturtle()
            car.penup()
        self.car_speed=self.car_speed+MOVE_INCREMENT





