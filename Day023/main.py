# Importing necessary classes and libraries.

from turtle import Screen
import time
from player import Player
from cars import Car
from levels import Levels

# Setting up the screen for the game.

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Cross")
screen.tracer(0)

# Setting up the turtle for the game.

car_list = []
challenger = Player()

# Creating the cars and appending them into a list.

for i in range(20):
    cars = Car()
    car_list.append(cars)

# Creating the level board and the while loop.

level = Levels()
game_is_on = True

while game_is_on:
    for car in car_list:
      
        # While game is on, cars consistently move. If they reach end of screen, they revert to start.
        
        car.move()
        car.take_car_back_to_start()
        
        # If you collide with a car, game is over.
        
        if (car.xcor() <= 50 or car.xcor() >= -50) and (challenger.distance(car) <= 20):
            game_is_on = False
            level.game_over()
            
    # Listening for keystrokes of the user to move turtle forward.
    
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(fun=challenger.up, key="Up")
    
# If turtle reaches the end of screen, the game goes to next level, where cars are faster.

    if challenger.ycor() >= 290:
        level.next_level()
        challenger.hideturtle()
        challenger.goto(0, -280)
        challenger.showturtle()
        for car in car_list:
            car.level_up()


screen.exitonclick()
