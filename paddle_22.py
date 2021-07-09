from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y_new = self.ycor() + 30
        self.sety(y_new)

    def go_down(self):
        y_new = self.ycor() - 30
        self.sety(y_new)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.speed(10)
        self.shapesize(0.8, 0.8)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.game_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.game_speed *= 0.8

    def change_position(self):
        self.home()
        self.game_speed = 0.1
        self.bounce_x()


