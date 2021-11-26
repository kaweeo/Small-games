# import colorgram
#
# colors = colorgram.extract('dot.jpg', 15)
# colors_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_rgb.append(new_color)
# print

import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

colors_list = [(231, 254, 242), (43, 1, 177), (78, 253, 172), (226, 149, 109),
               (230, 224, 253), (160, 3, 83), (3, 212, 100), (3, 139, 64), (246, 41, 128), (109, 108, 248),
               (252, 253, 53), (184, 184, 251), (211, 106, 4)]


# 10 by 10 dots, 20 in size, spaced on 50 paces


def turn_left():
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)

def turn_right():
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

def line_of_dots():
    for dot in range(10):
        dot_color = random.choice(colors_list)
        t.penup()
        t.dot(20, dot_color)
        t.forward(50)


screen.screensize(1000, 600)
t.penup()
t.setx(-400)
t.sety(-350)
t.speed("slowest")
for i in range(5):
    line_of_dots()
    turn_left()
    line_of_dots()
    turn_right()

screen.exitonclick()
