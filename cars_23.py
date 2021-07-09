from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "blue", "green", "purple", "pink", "grey"]
STARTING_DISTANCE = 5
MOVE_DISTANCE = 3


class Cars:
    def __init__(self):
        self.all_cars = []
        self.distance = STARTING_DISTANCE

    def create_car(self):
        random_num = randint(1, 6)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(1, 2)
            y_pos = randint(-250, 260)
            new_car.penup()
            new_car.goto(300, y_pos)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def moving(self):
        for car in self.all_cars:
            car.forward(self.distance)

    def level_speed(self):
        self.distance += MOVE_DISTANCE






