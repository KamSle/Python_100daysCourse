# 100 days with Python
# Turtle Graphics / Object states and instances
# DAY 19
from turtle import Turtle, Screen
from random import randint, choice

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick up a color: ")

colors = ["red", "green", "blue", "orange", "purple", "yellow"]
turtle_list = []
z = 0
for index in range(0, 6):
    pipp = Turtle(shape="turtle")
    pipp.color(colors[index])
    pipp.up()
    pipp.goto(x=-240, y=-100+z)
    z += 30
    turtle_list.append(pipp)
if user_bet:
    is_race_on = True

while is_race_on:
    random_distance = randint(0, 10)
    random_turtle = choice(turtle_list)
    random_turtle.forward(random_distance)
    if random_turtle.xcor() > 230.00:
        wining_color = random_turtle.pencolor()
        is_race_on = False
        print(f"The winner is: {random_turtle.pencolor()}!")
        if random_turtle.pencolor() == user_bet:
            print(f"You win! Your choice {user_bet} is the winner {random_turtle.pencolor()}")
        else:
            print(f"You lose! Your choice {user_bet} is not like the winner {random_turtle.pencolor()}")
        screen.bye()
screen.exitonclick()
