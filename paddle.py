from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.setup_paddle(pos)

    def setup_paddle(self, pos):
        self.penup()
        self.shape("square")
        self.setpos(pos)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
