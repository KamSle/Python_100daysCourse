# 100 days with Python
# Turtle Graphics / OOP / Snake Game
# DAY 20/21


from snake_20_21 import Mysnake
from food_20_21 import Food
from scoreboard_20_21 import Scoreboard
from turtle import Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("Snakee game")
screen.tracer(0)

snake = Mysnake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increasing_score()
        snake.extend()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()

    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
