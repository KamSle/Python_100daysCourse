from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.result_r = 0
        self.result_l = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.writing_score()

    def writing_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.result_l, True, align="center", font=("Courier", 28, "bold"))
        self.goto(100, 200)
        self.write(self.result_r, True, align="center", font=("Courier", 28, "bold"))

    def increase_r(self):
        self.result_r += 1
        self.writing_score()

    def increase_l(self):
        self.result_l += 1
        self.writing_score()

