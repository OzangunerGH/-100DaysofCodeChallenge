from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.create_scoreboard()
    


    def middle_line(self):
        self.pensize(5)
        self.goto(0,290)
        self.setheading(270)
        for i in range(0,290,15):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)


    def create_scoreboard(self):
        self.clear()
        self.goto(0, 350)
        self.write(arg=f"{self.score} ",align="center",font=("Arial", 60, "normal"))


    def increase_score(self):
        self.score += 20
        self.clear()
        self.create_scoreboard()

    def game_over(self):
        self.score = 0
        self.clear()
        self.goto(0, 330)
        self.write(arg=f"Sorry, game over.\n"
                       f"You lost!",align="center", font=("Arial", 40, "normal"))

    def level_up(self):
        self.clear()
        self.goto(0, 330)
        self.write(arg=f"Congratulations!\n"
                       f"You advance to the next level!", align="center", font=("Arial", 40, "normal"))




