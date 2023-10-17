from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.value = 0
        self.write(f"Score : {self.value}", True, align="center", font=("Arial", 15, "normal"))

    def score_update(self):
        self.clear()
        self.goto(0, 270)
        self.value += 1
        self.write(f"Score : {self.value}", True, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True, align="center", font=("Arial", 15, "normal"))