from turtle import *

class Scoreboard(Turtle):

    def __init__(self, board_width):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(board_width + 30, 0)

    def add_score(self,value):
        self.clear()
        self.score += value
        self.write(f"{self.score}")