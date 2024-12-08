
from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=240)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.l_score} | {self.r_score}", align="center", font=('Arial', 40, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.l_score == 5:
            self.update_scoreboard()
            self.goto(0, 0)
            self.write(arg=f"GAME OVER!\n Left player wins!", align="center", font=('Arial', 26, 'normal'))
            return True
        elif self.r_score == 5:
            self.update_scoreboard()
            self.goto(0, 0)
            self.write(arg=f"GAME OVER!\n Right player wins!", align="center", font=('Arial', 26, 'normal'))
            return True
        else:
            return False
