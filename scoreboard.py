from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=230)
        self.score = 0
        f = open("high_score.txt")
        self.highscore = int(f.read())
        f.close()
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", False, align="center")

    def update_score(self):
        self.score += 1

        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", False, align="center", font=('Arial', 25, 'normal'))

    def game_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            f = open("high_score.txt", "w")
            f.write(str(self.highscore))
            f.close()

        self.score = 0
        self.show_score()
