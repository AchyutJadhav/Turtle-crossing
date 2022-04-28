import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
# player.move()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")

car = CarManager()

score = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.car_generate()
    car.move_cars()
    screen.update()

    if player.ycor() > 300:
        score.increase_level()
        player.goto(0, -280)
        car.increase_speed()

    for i in car.all_cars:
        if player.distance(i) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()


