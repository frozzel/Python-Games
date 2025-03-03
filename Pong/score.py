from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("medium purple")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()
        
    def update_score(self):
        self.write(f"{self.player1_score}  {self.player2_score}", align="center", font=("Courier", 60, "normal"))   
             
    def increase_score(self, player):
        if player.xcor() < 0:
            self.player2_score += 1
        else:
            self.player1_score += 1
        self.clear()
        self.update_score()
        
    def game_over(self, player):
        if player == "player1":
            self.goto(0, 0)
            self.write("Player  1 Wins!", align="center", font=("Courier", 40, "normal"))
            
        else:
            self.goto(0, 0)
            self.write("Player  2 Wins!", align="center", font=("Courier", 40, "normal"))
        