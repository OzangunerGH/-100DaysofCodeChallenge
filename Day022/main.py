# Importing necessary classes and libraries.

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Setting up the game screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating required objects ( Paddle, ball, scoreboard)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Setting up a concurrent while loop to keep the game going.

game_is_on = True
while game_is_on:
    time.sleep(0.8)
    ball.setposition(0, 0)
    round_is_on = True

# while loop to keep the ball moving while the  current round of the game is ongoing. Listening for user keystrokes.
# Defining conditions to track paddle and wall collisions with the ball, and also keeping track of score.
    while round_is_on:
        time.sleep(0.1)
        ball.move()
        screen.update()
        screen.listen()
        screen.onkeypress(fun=player_1.go_down, key="Down")
        screen.onkeypress(fun=player_1.go_up, key="Up")
        screen.onkeypress(fun=player_2.go_down, key="2")
        screen.onkeypress(fun=player_2.go_up, key="8")
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.wall_bounce()
        if (ball.xcor() >= 350 or ball.xcor() <= -350) and (
                ball.distance(player_2) < 50 or ball.distance(player_1) < 50):
            ball.paddle_bounce()
        if ball.xcor() >= 400:
            scoreboard.increase_score_l()
            round_is_on = False
        if ball.xcor() <= -400:
            scoreboard.increase_score_r()
            round_is_on = False

screen.exitonclick()
