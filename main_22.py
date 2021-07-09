# 100 days with Python
# Turtle Graphics / OOP
# DAY 22
from turtle import Screen
from paddle_22 import Paddle, Ball
from scores_22 import Score

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.game_speed)
    screen.update()
    ball.move()
    # make the ball bounce when it touch the wall(up or down)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # make the ball bounce when it touch the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()
    # Right paddle misses the ball
    if ball.xcor() > 380:
        ball.change_position()
        score.increase_l()
    # Left paddle misses the ball
    if ball.xcor() < -380:
        ball.change_position()
        score.increase_r()

screen.exitonclick()
