from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").capitalize()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
position = 0

for turtle in range(6):
    tim = Turtle(shape="turtle")
    all_turtles.append(tim)
    tim.color(colors[turtle])
    tim.penup()
    tim.goto(-240, -120 + position)
    position += 40
if user_bet:
    
    is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            random_number = random.randint(0, 10)
            turtle.forward(random_number)
            turtle_position = turtle.xcor()
            if turtle_position > 230:
                winner_turtle = turtle.pencolor().capitalize()
                is_race_on = False
                print(f"{winner_turtle} turtle wins the race!")
                if winner_turtle == user_bet:
                    print("You win the bet.")
                else:
                    print(f"You lose the bet. Your guess: {user_bet} turtle")

screen.exitonclick()
