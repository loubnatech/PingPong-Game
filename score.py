from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.display_score()
    def display_score(self):
        self.clear()
        self.goto(200,200)
        self.write(self.r_score,font=("courier",40,"normal"),align="center")
        self.goto(-200,200)
        self.write(self.l_score,font=("courier",40,"normal"),align="center")
    def r_point(self):
        self.r_score+=1
        self.display_score()
    def l_point(self):
        self.l_score+=1
        self.display_score()