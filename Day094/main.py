# Importing necessary classes and libraries.

from turtle import Screen
from ship import Ship
from bullet import Bullet
import time
from scoreboard import Scoreboard
from aliens import Aliens


def exit_program():
    screen.bye()

# Setting Functionality Of the Main Program
def check_hit_aliens():
    """Checks if the bullet collides with any of the aliens. Increases score and deletes alien and the bullet from the screen if the collision hpapens."""
    global round_is_on, game_is_on
    for segment in aliens.segments:
        if bullet.ycor() > -350 and (bullet.distance(segment) < 10):
            segment.goto(10000, 10000)
            bullet.disappear()
            scoreboard.increase_score()
        if segment.ycor() <= -400:
            scoreboard.game_over()
            round_is_on = False
            game_is_on = False
        if scoreboard.score == 480:
            scoreboard.level_up()
            round_is_on = False
            game_is_on = True

def listen_for_keys():
    """Listens for Left and Right keys within the screen borders."""
    screen.onkeypress(fun=exit_program, key="Escape")
    screen.onkeypress(fun=lambda ship=player_1: bullet.fire(player_1), key="space")
    if player_1.xcor() <= -370:
        screen.onkeypress(fun=None, key="Left")
    else:
        screen.onkeypress(fun=player_1.go_down, key="Left")
    if player_1.xcor() >= 360:
        screen.onkeypress(fun=None, key="Right")
    else:
        screen.onkeypress(fun=player_1.go_up, key="Right")
def fire_bullet():
    """Fires a red bullet if you don't already have a bullet within your screen."""
    if bullet.ycor() < 500:
        bullet.move()
        screen.onkeypress(fun=None, key="space")
    elif bullet.ycor() >= 500:
        bullet.disappear()
        screen.onkeypress(fun=lambda ship=player_1: bullet.fire(player_1), key="space")


# Setting up the game screen.
screen = Screen()
screen.addshape("ship.gif")
screen.addshape("alien.gif")
screen.bgpic("bg_picture.gif")
screen.setup(width=800, height=900)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating coordinates of the bricks.

# Creating required objects ( Ship, bullet, scoreboard)
player_1 = Ship((0, -400))
player_1.shape("ship.gif")
bullet = Bullet()
bullet.goto(10000, 10000)
scoreboard = Scoreboard()
aliens = Aliens()
for alien in aliens.segments:
    alien.shape("alien.gif")
# Setting up a concurrent while loop to keep the game going.
game_is_on = True
while game_is_on:
    time.sleep(2)
    round_is_on = True
    # while loop to keep the bullet moving while the  current round of the game is ongoing. Listening for user keystrokes.
    # Defining conditions to track paddle and wall collisions with the bullet, and also keeping track of score.
    while round_is_on:
        time.sleep(0.01)
        listen_for_keys()
        aliens.move()
        fire_bullet()
        screen.update()
        screen.listen()
        check_hit_aliens()
    screen.mainloop()
    screen.exitonclick()
