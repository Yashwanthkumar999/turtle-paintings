import turtle
from turtle import Turtle,Screen
import random

tim = Turtle()
tim.hideturtle()

sc = Screen()
sc.setup(500,400)
user_guess=sc.textinput(title="make your bet", prompt="which turtle will win the race? enter a color :")

colors = ["red", "blue", "green", "purple", "pink","yellow","orange"]
y_positions = [-120,-80,-40,0,40,80,120]
players =[]
for i in range(0,7):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230, y=y_positions[i])
    players.append(tim)
is_race_on = True
winner = ""
while is_race_on:

    for player in players:

        player.forward(random.randint(0, 8))
        if player.xcor() >= 230:
            winner = player.pencolor()
            is_race_on = False
if user_guess == winner:
    print(f" you've won ! The winner is {winner} turtle !!")

else:
    print(f" you've lost ! The winner is {winner} turtle !!")






sc.exitonclick()










