from turtle import Turtle
##Creating the paddle class to create player paddles.


class Ship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.left(270)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setposition(position)
        self.setheading(0)



    def go_up(self):
         self.forward(10)


    def go_down(self):
        self.backward(10)










