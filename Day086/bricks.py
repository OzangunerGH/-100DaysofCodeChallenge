from turtle import Turtle
import random

##Creating the paddle class to create player paddles.

colors = ["red", "blue", "green", "yellow" ]


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.left(270)
        self.shapesize(stretch_wid=2, stretch_len=3)
        self.penup()
        self.setposition(position)
        self.setheading(0)
