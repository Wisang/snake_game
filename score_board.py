from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align="center", font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 20, 'normal'))



