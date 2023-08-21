from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x=x, y=y)

    def up(self):
        cur_y = self.ycor()
        new_y = cur_y + 20
        self.goto(self.xcor(), y=new_y)

    def down(self):
        cur_y = self.ycor()
        new_y = cur_y - 20
        self.goto(self.xcor(), y=new_y)

