from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
         