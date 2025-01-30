from turtle import Turtle

TURTLE_COORDS = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = list()
        self.make_body()
        self.head = self.segments[0]

    def make_body(self):
        for i in TURTLE_COORDS:
            self.add_segment(i)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[seg_num - 1].xcor()
            ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(xcor, ycor)
        self.segments[0].forward(DISTANCE)

    def add_segment(self, position):
        new_turt = Turtle(shape="square")
        new_turt.penup()
        new_turt.color("white")
        new_turt.goto(position)
        self.segments.append(new_turt)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



