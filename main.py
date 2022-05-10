# Importing necessary classes and libraries.

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from bricks import Brick


def exit_program():
    screen.bye()

# Setting up the game screen.
screen = Screen()
screen.setup(width=800, height=900)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating coordinates of the bricks.
position = []
for posy in range(300, 140, -40):
    for posx in range(-380, 380, 60):
        position.append((posx, posy))

#Creating the bricks and appending them to a list.
bricks = []
for item in position:
    brick = Brick(position=item)
    bricks.append(brick)

# Creating required objects ( Paddle, ball, scoreboard)
player_1 = Paddle((0, -400))
ball = Ball()
scoreboard = Scoreboard()

# Setting up a concurrent while loop to keep the game going.
game_is_on = True
while game_is_on:
    time.sleep(2)
    ball.setposition(0, 0)
    round_is_on = True
    # while loop to keep the ball moving while the  current round of the game is ongoing. Listening for user keystrokes.
    # Defining conditions to track paddle and wall collisions with the ball, and also keeping track of score.
    while round_is_on:
        time.sleep(0.01)
        ball.move()
        screen.update()
        screen.listen()
        screen.onkeypress(fun=exit_program, key="Escape")
        screen.onkeypress(fun=player_1.go_down, key="Left")
        screen.onkeypress(fun=player_1.go_up, key="Right")
        if ball.ycor() > 450:
            ball.wall_bounce()
        if ball.xcor() > 390 or ball.xcor() < -400:
            ball.paddle_bounce()
        if (ball.ycor() <= -390) and (ball.distance(player_1) < 70):
            ball.wall_bounce()
        if ball.ycor() <= -450:
            round_is_on = False
        for brick in bricks:
            if ball.ycor() > 0 and (ball.distance(brick) < 40):
                brick.goto(10000,10000)
                ball.wall_bounce()
                scoreboard.increase_score()
        if scoreboard.score == 1040:
            scoreboard.next_level()
            time.sleep(2)
            round_is_on = False
            for item in position:
                brick = Brick(position=item)
                bricks.append(brick)
            scoreboard.create_scoreboard()


screen.exitonclick()
