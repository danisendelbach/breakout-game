from turtle import *

class Ball(Turtle):
    def __init__(self, board_width, board_height):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,-190)
        self.shapesize(.5,.5)
        self.setheading(60)


        self.board_width = board_width
        self.board_height = board_height

    def bounce_horizontal(self):
        self.setheading(-self.heading())

    def bounce_vertical(self):
        self.setheading(-self.heading()+180)

    def detect_paddle(self, paddle):
        if -190 >= self.ycor() >= -210 and paddle.right_edge - 5 < self.xcor() < paddle.right_edge + 5:
            self.bounce_vertical()

        if -190 >= self.ycor() >= -210 and paddle.left_edge - 5 < self.xcor() < paddle.left_edge + 5:
            self.bounce_vertical()

        if -195+5 >= self.ycor() >= -200 and paddle.left_edge <= self.xcor() <= paddle.right_edge:
            self.bounce_horizontal()


    def if_obstacle_detected(self,obstacle,score):
        score.add_score(obstacle.value+1)
        obstacle.goto(1000, 1000)
        obstacle.get_edges()
    def detect_obstacle(self, obstacle_collection, score):
        for obstacle in obstacle_collection:
            if obstacle.ycor()+10 >= self.ycor() >= obstacle.ycor()-10 and \
                    obstacle.right_edge - 5 < self.xcor() < obstacle.right_edge + 5:
                self.bounce_vertical()
                self.if_obstacle_detected(obstacle,score)
                return True


            if obstacle.ycor()+10 >= self.ycor() >= obstacle.ycor()-10 and \
                    obstacle.left_edge - 5 < self.xcor() < obstacle.left_edge + 5:
                self.bounce_vertical()
                self.if_obstacle_detected(obstacle,score)
                return True


            if obstacle.top_edge >= self.ycor() >= obstacle.ycor() and \
                    obstacle.left_edge <= self.xcor() <= obstacle.right_edge:
                self.bounce_horizontal()
                self.if_obstacle_detected(obstacle,score)
                return True


            if obstacle.bottom_edge <= self.ycor() <= obstacle.ycor() and \
                    obstacle.left_edge <= self.xcor() <= obstacle.right_edge:
                self.bounce_horizontal()
                self.if_obstacle_detected(obstacle,score)
                return True

        return False


    def detect_wall(self):
        x = self.xcor()
        y = self.ycor()

        if abs(x) >= self.board_width:
            print(x,y,"--->detected")
            self.bounce_vertical()


        if y > self.board_height:
            self.bounce_horizontal()

    #def detect_up_wall(self):