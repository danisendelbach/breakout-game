from turtle import *

PACE = 30
WIDTH = 100
HEIGHT = 5
class Paddle(Turtle):
    def __init__(self, board_with):
        super().__init__()
        self.penup()
        self.goto(0,-200)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=HEIGHT/10, stretch_len=WIDTH/10)

        self.right_edge = self.xcor()+WIDTH
        self.left_edge = self.xcor()-WIDTH

        self.board_width = board_with

    def move_right(self):
        if self.right_edge < self.board_width :
            self.forward(PACE)
            self.right_edge = self.xcor() + WIDTH
            self.left_edge = self.xcor() - WIDTH

    def move_left(self):
        print(self.board_width, self.left_edge)
        if self.left_edge > -self.board_width:
            self.backward(PACE)
            self.right_edge = self.xcor() + WIDTH
            self.left_edge = self.xcor() - WIDTH
