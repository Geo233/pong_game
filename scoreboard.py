from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.goto(-50, 200)
        self.write(self.lscore, align= "center", font =("Arial", 50, "bold"))
        self.goto(50, 200)
        self.write(self.lscore, align="center", font=("Arial", 50, "bold"))

    def score_update(self):
        self.goto(-50, 200)
        self.write(self.lscore, align="center", font=("Arial", 50, "bold"))
        self.goto(50, 200)
        self.write(self.rscore, align="center", font=("Arial", 50, "bold"))
