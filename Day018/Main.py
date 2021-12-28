from turtle import Turtle, Screen
import random
billy = Turtle()
screen = Screen()
screen.colormode(255)
billy.speed("fastest")
billy.penup()
billy.hideturtle()

## Extracted the color scheme from one of the paintings of Damien Hirst in a tuple format by using colorgram package.

color_list = [(249, 248, 248), (237, 241, 245), (238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17),
              (218, 127, 106),
              (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
              (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33),
              (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216),
              (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216),
              (100, 218, 229), (117, 171, 192), (79, 135, 178)
              ]

for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        billy.pencolor(random.choice(color_list))
        billy.setposition(x, y)
        billy.dot(20)


screen.exitonclick()
