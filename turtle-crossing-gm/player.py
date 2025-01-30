from turtle import Turtle as turt

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turt):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.go_begin()
        self.setheading(90)

    def go_begin(self):
        self.goto(STARTING_POSITION)

    def up(self):
        y_coord = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=y_coord)


