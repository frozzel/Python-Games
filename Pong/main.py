from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from center_line import draw_center_line
import time

# Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player1 = Paddle((-350, 0))
player2 = Paddle((350, 0))
center_line = draw_center_line()
ball = Ball()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    









screen.exitonclick()