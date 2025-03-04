from turtle import Turtle


class YellowLines(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("yellow")
        self.pensize(5)
        self.penup()
        self.goto(position)
        self.setheading(360)
        self.draw_lines()
        
    def draw_lines(self):
        for i in range(15):
            self.pendown()
            self.forward(500)
            