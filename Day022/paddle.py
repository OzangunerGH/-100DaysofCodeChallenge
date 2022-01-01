from turtle import Turtle
##Creating the paddle class to create player paddles.

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.setposition(position)


    def go_up(self):
         self.forward(20)


    def go_down(self):
        self.backward(20)










