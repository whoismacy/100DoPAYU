import time

from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# Setting Screen requirements
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Creating an instance of paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Creating an instance of a ball
ball = Ball()

# Creating an instance of the scoreboard
scoreboard = ScoreBoard()

# Listening to user action
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# While loop to update the screen
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or  ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle (right)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when paddle misses left
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Screen's exit
screen.exitonclick()
