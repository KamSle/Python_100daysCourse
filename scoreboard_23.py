from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.writing_level()
        self.game_over = "GAME OVER"

    def writing_level(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Level: {self.level}", True, align="center", font=FONT)

    def game_over_now(self):
        self.goto(0, 0)
        self.write(self.game_over, True, align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.goto(-230, 260)
        self.level += 1
        self.write(f"Level: {self.level}", True, align="center", font=FONT)
