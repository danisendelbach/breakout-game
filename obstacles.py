from turtle import *
import math
OBSTACLE_WIDTH = 30
DISTANCE_X = 2*OBSTACLE_WIDTH + 10
START_Y = 0

class Obstacle(Turtle):

    def __init__(self, obstacle_collection, num_col):
        super().__init__()
        self.penup()
        self.shape("square")
        self.posx = -(OBSTACLE_WIDTH*num_col)
        self.posy = START_Y

        self.columns = num_col
        self.shapesize(stretch_wid=1, stretch_len=OBSTACLE_WIDTH/10)
        self.obstacle_collection = obstacle_collection
        self.row_id = 0
        self.col_id = 0

        self.value = 0

        self.place()

        self.set_color()

        self.get_edges()

    def place(self):
        if len(self.obstacle_collection) != 0:
            last_object = self.obstacle_collection[-1]

            self.col_id = last_object.col_id
            self.row_id = last_object.row_id

            if self.col_id == self.columns-1:
                self.col_id = 0
                self.row_id = self.row_id + 1

            else:
                self.col_id = self.col_id + 1

        self.posx += self.col_id * DISTANCE_X
        self.posy += self.row_id * 40

        self.speed("fastest")
        self.goto(self.posx, self.posy)


    def set_color(self):
        self.colors = {
            0: "blue",
            1: "green",
            2: "yellow"
        }
        divisor = math.ceil(self.columns // 3)+1
        self.value = (self.row_id // divisor)
        self.color(self.colors[self.value])

    def get_edges(self):

        self.top_edge = self.ycor() + 20
        self.bottom_edge = self.ycor() - 20
        self.left_edge = self.xcor() - 30
        self.right_edge = self.xcor() + 30




