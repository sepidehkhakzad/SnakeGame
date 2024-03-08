from turtle import Turtle

START_SCORE = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.pu()
        self.color("white")
        self.ht()
        self.score = 0
        self.write_score()
        # self.goto(60, 270)

    def increase_score(self):
        self.score = self.score + 1
        self.undo()
        self.write_score()

    def write_score(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 20, 'normal'))

    def game_over(self):
        self.undo()
        self.goto(0, 0)
        self.write(f"Game Over! Final Score: {self.score}", move=False, align="center", font=('Courier', 20, 'normal'))
