
import turtle as t
import random
tim = t.Turtle()
tim.speed("fastest")
colors = ["red", "blue", "green", "purple", "pink","yellow","orange"]
for i in range(100):
    tim.pensize(5)
    current_heading = tim.heading()
    tim.color(random.choice(colors))
    tim.circle(100)
    tim.setheading(current_heading+10)




sc =t.Screen()
sc.exitonclick()