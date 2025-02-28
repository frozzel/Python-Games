from turtle import Turtle

def draw_center_line():
    center_line = Turtle()
    center_line.color("white")
    center_line.penup()
    center_line.goto(0, 300)
    center_line.setheading(270)
    center_line.pensize(6)
    while center_line.ycor() > -300:
        center_line.pendown()
        center_line.forward(20)
        center_line.penup()
        center_line.forward(20)
        
    center_line.hideturtle()