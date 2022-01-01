
from turtle import Turtle


class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.pencolor("black")
        self.goto(-280, 270)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=("Arial", 16, "bold"))

    def next_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over.", align="Center", font=("Arial", 24, "bold"))

