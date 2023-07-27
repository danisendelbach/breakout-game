from turtle import *

class WallDrawer(Turtle):
    def __init__(self,board_width, board_height):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-board_width, -board_height)
        self.pendown()
        self.goto(-board_width, board_height)
        self.goto(board_width,board_height)
        self.goto(board_width,-board_height)
        self.goto(-board_width,-board_height)
