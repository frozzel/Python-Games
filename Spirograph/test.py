import turtle as t
from turtle import  Screen
import random

timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.color("red")

# Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# def draw_shape(sides, color):
#     timmy.color(color)
#     angle = 360 / sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)

# color_choices = ["red", "blue", "green", "yellow", "purple", "orange", "black", "pink"]

# for i in range(3, 11):
#     color = random.choice(color_choices)
#     draw_shape(i, color)

# Draw a random walk
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# timmy.pensize(15)
# timmy.speed("fastest")
# directions = [0, 90, 180, 270]

# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# Draw a Spirograph
timmy.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        
draw_spirograph(1)



screen = Screen()
screen.exitonclick()
