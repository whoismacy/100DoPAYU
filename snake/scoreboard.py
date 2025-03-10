from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Montserrat', 14, 'bold')

class ScoreBoard(Turtle):
    def  __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

