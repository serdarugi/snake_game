from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreTable(Turtle):
    def __init__(self):
        super().__init__()
        self.score_screen = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)

    def create_score(self):
        self.write(f"Score : {self.score_screen}", False, ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, ALIGNMENT, font=FONT)
