import turtle as t
from turtle import  Screen

timmy = t.Turtle()

def move_forward():
    timmy.forward(10)
    
def move_backward():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)
    
def clear_reset():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_reset)

screen.exitonclick()