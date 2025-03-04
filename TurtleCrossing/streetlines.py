from turtle import Turtle   

class StreetLines(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(360)
        self.draw_lines()
        
        
    def draw_lines(self):
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            
    