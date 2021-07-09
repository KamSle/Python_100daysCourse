from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(1,1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed(10)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() > FINISH_LINE:
            self.goto(STARTING_POSITION)
            return True




