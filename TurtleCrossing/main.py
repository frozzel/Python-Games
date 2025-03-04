import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from streetlines import StreetLines
from yellowlines import YellowLines

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("dim gray")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

for i in range(15):
    streetlines = StreetLines((-300, -260 + i * 40))

lines = [(-300, 0), (-300, -260), (-300, 260) ]

for line in lines:
    yellowlines = YellowLines(line)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    if player.ycor() > 280:
        player.goto(0, -280)
        player.setheading(90)
        scoreboard.level_up()
        car_manager.level_up()   
        
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            
screen.exitonclick()