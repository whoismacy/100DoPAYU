import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create Player
player = Player()

# Create ScoreBoard
scoreboard = ScoreBoard()

#Create Car
car = CarManager()

# Moving up Listener
screen.listen()
screen.onkey(fun=player.up, key="Up")

# Count
count = 0

# Game Variable
game_is_on = True

# Game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1

# Move the Cars
    car.move_segments()

# Turtle getting to the end of the screen
    if player.ycor() >= 280:
        player.go_begin()
        scoreboard.incrs_show_score()
        car.increase_speed()

# Increasing the Cars
    if count % 9 == 0:
        car.gen_segments()

# if turtle collides with one of the blocks.
    for car_obj in car.segments:
        if car_obj.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
