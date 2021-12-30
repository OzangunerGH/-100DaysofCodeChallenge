from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def wall_collision(self):
        if self.head.xcor() > 299 or self.head.xcor() < -299 or self.head.ycor() > 299 or self.head.ycor() < -299:
            return True
        else:
            return False

    def tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() == 270:
            self.head.right(90)
        else:
            self.head.left(90)

    def right(self):
        if self.head.heading() == 270:
            self.head.left(90)
        else:
            self.head.right(90)

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)

    def extend(self):
        self.add_segment(self.segments[-1].position())
