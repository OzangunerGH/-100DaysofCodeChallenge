from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.fillcolor("white")
        self.color("white")
        self.speed("slow")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor () + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)


    def paddle_bounce(self):
        self.xmove *= -1


    def wall_bounce(self):
        self.ymove *= -1


