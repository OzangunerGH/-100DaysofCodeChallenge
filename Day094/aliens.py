from turtle import Turtle
import random

##Creating the paddle class to create player paddles.
POSITIONS = [(-380, 300), (-320, 300), (-260, 300), (-200, 300), (-140, 300), (-80, 300), (-380, 260), (-320, 260), (-260, 260), (-200, 260), (-140, 260), (-80, 260), (-380, 220), (-320, 220), (-260, 220), (-200, 220), (-140, 220), (-80, 220), (-380, 180), (-320, 180), (-260, 180), (-200, 180), (-140, 180), (-80, 180)]
colors = ["green"]
MOVE_DISTANCE = 50


#Creating the bricks and appending them to a list.

class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.hideturtle()
        self.create_aliens()
        self.head = self.segments[-1]
        self.movement = 0
        self.tour = 0


    def add_alien(self,position):
        new_alien = Turtle("circle")
        new_alien.color(random.choice(colors))
        new_alien.left(270)
        new_alien.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_alien.penup()
        new_alien.setheading(0)
        new_alien.setposition(position)
        self.segments.append(new_alien)


    def create_aliens(self):
        for pos in POSITIONS:
            self.add_alien(position=pos)

    def move(self):
        self.movement += 1
        for segment in self.segments:
            segment.forward(3)
        if self.movement == 150:
            self.change_direction()


    def change_direction(self):
        self.movement = 0
        for segment in self.segments:
            if segment.heading() == 180:
                segment.setheading(0)
            elif segment.heading() == 0:
                segment.setheading(180)
        self.tour += 1
        if self.tour == 2:
            self.move_forward()

    def move_forward(self):
        for segment in self.segments:
            segment.goto(segment.xcor(), segment.ycor() -56)
        self.tour = 0

    def disappear(self):
        self.goto(10000,10000)








