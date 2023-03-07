from turtle import Turtle, Screen
import time
from paddle import Paddle
from board import Board
from ball import Ball

PADDLE_LEFT_POSITION = (350, 0)
PADDLE_RIGHT_POSITION = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle(PADDLE_LEFT_POSITION)
paddle_right = Paddle(PADDLE_RIGHT_POSITION)
score_board = Board()
ball = Ball()

screen.listen()
screen.onkeypress(paddle_left.up, "Up")
screen.onkeypress(paddle_left.down, 'Down')
screen.onkeypress(paddle_right.up, "w")
screen.onkeypress(paddle_right.down, 's')

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        score_board.increment_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.increment_r_score()

    if ball.is_collide_paddle(paddle_left) or ball.is_collide_paddle(paddle_right):
        ball.bounce_x()

screen.exitonclick()
