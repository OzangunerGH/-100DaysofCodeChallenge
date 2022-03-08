from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)


@app.route('/')
def homepage():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif></img>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_num:
        return "<h1 style='color: yellow'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_num:
        return "<h1 style='color: orange'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif guess == random_num:
        return "<h1 style='color: blue'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
