# 100 days with Python
# Turtle Graphics / OOP / Turtle crossing game
# DAY 23
from turtle import Screen
from player_23 import Player
from cars_23 import Cars
from scoreboard_23 import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)

player = Player()
car = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.moving()
    # player hit the car the game stops and we see game over
    for auto in car.all_cars:
        if auto.distance(player) < 20:
            score.game_over_now()
            game_on = False
    # player gets to the finish and gets to the start, level and speed goes up
    if player.finish():
        score.increase_level()
        car.level_speed()

screen.exitonclick()
