import random
from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.fillcolor("red")
        self.color("red")
        self.speed("slow")
        self.penup()
        self.turtlesize(0.4,0.4)
        self.hideturtle()
        self.setposition(10000, 10000)
        self.xmove = 0
        self.ymove = 15

    def move(self):
        new_x = self.xcor () + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)


    def paddle_bounce(self):
        self.ymove *= -1

    def wall_bounce(self):
        self.xmove *= -1


    def fire(self, ship):
            self.hideturtle()
            self.setposition(ship.xcor(), ship.ycor()+30),
            self.showturtle()

    def disappear(self):
        self.hideturtle()
        self.goto(1000, 1000)






