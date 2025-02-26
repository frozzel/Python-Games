from turtle import Screen
import turtle as t
import random
import tkinter 
from tkinter import messagebox


screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win: red, orange, yellow, green, blue, purple?")

# Create 6 turtles
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):
    new_turtle = t.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(turtle_colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i * 40)
    turtles.append(new_turtle)

# Start the Race


def start_race():
    run = True
    while run:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() > 230:
                run = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    # screen.textinput(title=f"You've won! The {winning_color} turtle is the winner!", prompt=" Congratulations! You've won!")
                    messagebox.showinfo(title="Congratulations!", message=f"You've won! The {winning_color} turtle is the winner!")
                    break
                else:
                    messagebox.showinfo(title="You've lost!", message=f"The {winning_color} turtle is the winner! Better luck next time!")
                    # screen.textinput(title=f"You've lost! The {winning_color} turtle is the winner!", prompt="Better luck next time!")
                    break
  
    
if user_bet:          
    start_race()


    










screen.exitonclick()
