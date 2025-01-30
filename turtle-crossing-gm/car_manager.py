import random

from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = .5


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.segments = list()
        self.gen_segments()

    @staticmethod
    def random_color():
        colour = COLORS[random.randint(a=0, b=len(COLORS) - 1)]
        return colour

    @staticmethod
    def rand_pos():
        y_coord = random.randint(a=-230, b=250)
        x_coord = random.randint(a=120, b=300)
        return x_coord, y_coord

    def gen_segments(self):
        for i in range(0, 2):
            turt = Turtle("square")
            turt.penup()
            turt.color(self.random_color())
            turt.shapesize(stretch_len=2, stretch_wid=1)
            turt.goto(self.rand_pos())
            self.segments.append(turt)

    def move_segments(self):
        for segment in self.segments:
            x_cor = segment.xcor() + (self.speed * -1)
            y_cor = segment.ycor()
            segment.goto(x_cor, y_cor)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def collision_detection(self, turt_obj):
        for seg in self.segments:
            if seg.position(turt_obj) < 4:
                return True


