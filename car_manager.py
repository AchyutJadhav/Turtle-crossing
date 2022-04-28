import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_generate(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.turtlesize(stretch_wid=1, stretch_len=2)
            y_cor = random.randint(-250, 250)
            car.goto(300, y_cor)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        self.move_cars()

