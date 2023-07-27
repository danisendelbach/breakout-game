from turtle import *
from turtle import update
from paddle import Paddle
from obstacles import Obstacle
from ball import Ball
import time
from walldrawer import WallDrawer
from scoreboard import Scoreboard

COLUMNS = 8
ROWS = 8
BOARD_WIDTH = 280
BOARD_HEIGHT = 280

screen = Screen()
screen.bgcolor("black")
wall_drawer = WallDrawer(board_width=BOARD_WIDTH, board_height=BOARD_HEIGHT)

obstacle_collection = []
for _ in range(COLUMNS * ROWS):
    new_obstacle = Obstacle(obstacle_collection,COLUMNS)
    obstacle_collection.append(new_obstacle)




paddle = Paddle(board_with=BOARD_WIDTH)
screen.listen()
screen.onkeypress(key="Right", fun=paddle.move_right)
screen.onkeypress(key="Left", fun=paddle.move_left)

ball = Ball(board_width=BOARD_WIDTH, board_height=BOARD_HEIGHT)
scoreboard = Scoreboard(BOARD_WIDTH)
scoreboard.add_score(0)
screen.tracer(0)
while True:

    screen.update()
    time.sleep(0.00001)
    if ball.ycor() <= -BOARD_HEIGHT:
        ball.hideturtle()
        paddle.goto(0,-200)
        ball = Ball(board_width=BOARD_WIDTH,board_height=BOARD_HEIGHT)
    ball.forward(3)
    ball.detect_wall()
    ball.detect_obstacle(obstacle_collection=obstacle_collection, score=scoreboard)


    ball.detect_paddle(paddle)


screen.exitonclick()