import turtle
import turtle as t
import random

tom = t.Turtle()
tom.shape("turtle")
sc = t.Screen()
tom.pensize(5)
tom.color("blue")
t.colormode(255)
colors = ['blue',"red","green","orange"]
directions = [0, 90, 180, 270]
def random_walk():
    for i in range(50):
        tom.setheading(random.choice(directions))
        tom.color(random.choice(colors))
        tom.hideturtle()
        tom.dot(10)
        tom.forward(50)


def spirograph():
    choose = sc.textinput(title="how many figures do you want ?", prompt="enter the number :")
    for i in range(3, int(choose)):
        tom.pensize(4)
        tom.setheading(0)
        tom.setheading(360 / i)
        tom.forward(40)

def move():
    tom.setheading(0)
    tom.forward(20)

def back():
    tom.setheading(180)
    tom.forward(20)

def up():
    tom.setheading(90)
    tom.forward(20)


def down():
    tom.setheading(270)
    tom.forward(20)
def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()
sc.listen()
sc.onkey(move, "space")

sc.onkey(back,"b")
sc.onkey(up,"u")
sc.onkey(down,"d")
sc.onkey(clear,"c")
sc.onkey(random_walk, "w")
sc.onkey(spirograph, "s")

sc.exitonclick()