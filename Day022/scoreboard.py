from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
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
        self.middle_line()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score} ",align="center",font=("Arial", 60, "normal"))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}",align="center",font=("Arial", 60, "normal"))


    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.create_scoreboard()


    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.create_scoreboard()

