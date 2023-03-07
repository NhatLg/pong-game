from turtle import Turtle
import random

WIDTH = 20
HEIGHT = 20
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 5
        self.move_speed = 0.1

    def is_collide_paddle(self, paddleObject):
        result = False
        if self.distance(paddleObject) < 50 and self.xcor() > 320:
            result = True
        elif self.distance(paddleObject) < 50 and self.xcor() < -320:
            result = True
        return result

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.x_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self._increase_speed()

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self._reset_speed()
        self.y_move *= -1

    def _increase_speed(self):
        self.move_speed *= 0.9

    def _reset_speed(self):
        self.move_speed = 0.1
