import turtle

class State(turtle.Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.state_name = state_name
        self.x = x
        self.y = y
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(state_name)
        # self.showturtle()
        
    def __str__(self):
        return self.state_name
    