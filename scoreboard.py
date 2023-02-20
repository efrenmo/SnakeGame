from turtle import Turtle
import art


ALIGNMENT= "center"
FONT = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.color("White")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, -100)

        self.write(art.GAME_OVER, align=ALIGNMENT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

