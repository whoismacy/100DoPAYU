from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-220, 220)
        self.level = 0
        self.incrs_show_score()

    def incrs_show_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="right", font=FONT)
        self.goto(-220, 220)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)

