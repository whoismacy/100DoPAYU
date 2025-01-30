from turtle import Turtle as turt
class Paddle(turt):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.position = position
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.goto(position)

    def move_up(self):
        y_cor = self.ycor() + 20
        self.goto(y=y_cor, x=self.xcor())

    def move_down(self):
        y_cor = self.ycor() - 20
        self.goto(y=y_cor, x=self.xcor())

