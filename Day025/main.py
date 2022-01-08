from turtle import Turtle, Screen
import pandas
import csv

# Setting up the Turtle
turtle = Turtle()
turtle.penup()
turtle.hideturtle()

# setting Up The Screen
screen = Screen()
screen.bgpic("blank_states_img.gif")

# Setting up the list from CSV Data
states_csv = pandas.read_csv("50_states.csv")
states_list = states_csv["state"]
states_list = states_list.tolist()
correct_guesses = []
missing_states = []
user_input = ""
# Main algorithm of the states game.
while user_input != "Exit" and len(correct_guesses) < 50:
    user_input = screen.textinput(title="Guess the State", prompt="Enter a states name").title()
    if user_input in states_list:
        correct_guesses.append(user_input)
        state_data = states_csv[states_csv.state == user_input]
        x_coordinate = int(state_data.x)
        y_coordinate = int(state_data.y)
        turtle.goto(x_coordinate, y_coordinate)
        turtle.write(user_input)
for states in states_list:
    if states not in correct_guesses:
        missing_states.append(states)
df = pandas.DataFrame(missing_states)
df.to_csv("Missed_States.csv")

if len(correct_guesses) == 50:
    print("Congratulations, you have guessed all 50 states!")

screen.exitonclick()
