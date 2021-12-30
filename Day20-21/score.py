from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(arg=f"Score is:  {self.score}", move=False, align="center", font=("Arial", 20, "bold"))

    def add_score(self):
        self.goto(0, 270)
        self.score += 1
        self.clear()
        self.write(f"Score is:  {self.score}", True, align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", True, align="center", font=("Arial", 20, "bold"))
