from turtle import Turtle, Screen
from random import choice
import colorgram

colors = colorgram.extract('image.jpg', 20)  # extract colors from the image using colorgram module
color_list = []
for color_obj in colors:
    color_list.append(tuple(color_obj.rgb))

# create turtle draw object
dot = Turtle()
dot.hideturtle()
screen = Screen()
screen.colormode(255)
dot.speed("fastest")
y = -200
x = -220
dot.penup()
dot.goto(x, y)  # move the turtle object to somewhere left-bottom(-200, -220) of the screen before drawing.

# the image will be a 10x10 image.
for row in range(10):  # for each row draw color dots
    for column in range(10):  # for each column draw a dot with a random color from color_list
        dot.dot(20, choice(color_list))
        dot.penup()
        dot.forward(50)
        dot.pendown()
    y += 50
    dot.penup()
    dot.goto(x, y)


screen.exitonclick()
