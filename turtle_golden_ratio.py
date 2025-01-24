from turtle import Turtle, Screen

import math

import random

amy = Turtle()
amy.speed(0)
amy.hideturtle()
screen = Screen()
screen.colormode(255)

def color_func(i):
    r = int(((math.sin(i * random.random()) + 1) / 2) * 255)
    g = int(((math.cos(i * random.random()) + 1) / 2) * 255)
    b = int(((math.cos(i * random.random()) + 1) / 2) * 255)
    return r,g,b

def polyline_colorful(n_sides, length, angle):
    for i in range(n_sides):
        amy.pencolor(color_func(i))
        amy.forward(length)
        amy.left(angle)
        length += 3

def polyline(n_sides, length, angle):
    for i in range(n_sides):
        amy.forward(length)
        amy.left(angle)
        length += 3


screen.setup(1920, 1080)
polyline_colorful(900, 1, 137.5)
screen.exitonclick()
