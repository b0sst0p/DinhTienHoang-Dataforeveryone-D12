from turtle import Turtle, Screen
from itertools import cycle
colors = ["green"]
def spiral(turtle, radius, color_names):
    colors = cycle(color_names)

    for _ in range(360 // 7):
        turtle.color()
        turtle.circle(radius)
        turtle.left(7)
yertle = Turtle(visible=False)
yertle.speed("fastest")
spiral(yertle, 50, colors)
screen = Screen()
screen.exitonclick()