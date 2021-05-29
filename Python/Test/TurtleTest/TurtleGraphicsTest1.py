import time
import turtle
turtle.speed(0)
turtle.hideturtle
turtle.penup()
turtle.setpos(-500,0)
turtle.pendown()
turtle.speed(1)
while True:
    turtle.pen(fillcolor="black", pencolor="black", pensize=10)
    turtle.forward(1000)
    turtle.pen(fillcolor="black", pencolor="red", pensize=10)
    turtle.backward(1000)