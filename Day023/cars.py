from turtle import Turtle
import random
CAR_COLORS = ["red","blue","yellow","green","orange","purple"]
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(CAR_COLORS))
        self.random_position()
        self.car_speed = START_MOVE_DISTANCE




    def random_position(self):
        random_y = random.randint(-250,270)
        random_x = random.randint(-280, 600)
        self.goto(random_x,random_y)

    def move(self):
        self.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    def take_car_back_to_start(self):
        random_y = random.randint(-250, 270)
        if self.xcor() < -400:
            self.goto(310,random_y)



