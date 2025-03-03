from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
from center_line import draw_center_line
import time

# Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("cornflower blue")
screen.title("Pong")
screen.tracer(0)


player1 = Paddle((-350, 0), "orchid")
player2 = Paddle((350, 0), "turquoise")
center_line = draw_center_line()
ball = Ball()
score = Score()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(player1) < 50 and ball.xcor() < -320 or ball.distance(player2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.xcor() > 380:
        if score.player1_score == 2:
            # score.increase_score(player2)
            game_is_on = False
            pass
        score.increase_score(player2)
        ball.reset_position()
    if ball.xcor() < -380:
        if score.player2_score == 2:
            # score.increase_score(player1)
            game_is_on = False 
            pass
        score.increase_score(player1)
        ball.reset_position()
  
    
if score.player1_score == 3:
    score.game_over("player1")
else:
    score.game_over("player2")
        
screen.exitonclick()