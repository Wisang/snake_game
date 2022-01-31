from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        # self.high_score = 0
        # with open("data.txt") as file:
        #     self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                file.write(str(self.score))
            # self.high_score = self.score
        self.score = 0

        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, align="center", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1

    def update_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=('Arial', 20, 'normal'))




