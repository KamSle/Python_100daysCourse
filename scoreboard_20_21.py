from turtle import Turtle
FONT = ("Courier", 15, "bold")
ALIGNMENT = "center"
POS = (0.0, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.result = 0
        with open("score_notebook_20_21.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(POS)
        self.writing_score()

    def writing_score(self):
        self.clear()
        self.write(f"Score: {self.result}  High score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def increasing_score(self):
        self.result += 1
        self.goto(POS)
        self.writing_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.result > self.high_score:
            self.high_score = self.result
            with open("score_notebook_20_21.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.result = 0
        self.goto(POS)
        self.writing_score()
