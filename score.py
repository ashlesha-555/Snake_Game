from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.color("cyan")
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score> self.highscore:
            self.highscore=self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    #def game_over(self):
     #   self.goto(0, 0)
      #  self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

