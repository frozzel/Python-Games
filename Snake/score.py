from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.score = 0
        # self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(f"{self.high_score}"))
        self.score = 0
        self.clear()
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))