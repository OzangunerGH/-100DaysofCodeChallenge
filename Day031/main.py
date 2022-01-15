# Importing Necessary Libraries.
import pandas
from tkinter import *
import random

# GLOBAL VARIABLES.
RAND_WORD = {}
BACKGROUND_COLOR = "#B1DDC6"

# Opening the relevant CSV file that has the words and write them in a dictionary.
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("data/french_words.csv")
    to_learn = pandas.DataFrame.to_dict(data_file, orient="records")
else:
    to_learn = pandas.DataFrame.to_dict(data_file, orient="records")


def new_random_word():
    """A function to generate random words from a list of wards and then print them to the flash card. """
    global RAND_WORD
    if len(to_learn) > 0:
        RAND_WORD = random.choice(to_learn)
        print_card()
    else:
        print("No words left to guess. Congratulations!")
        return


def correct_guess():
    """A function to delete the words that are correctly guessed by user so the word does not show up again."""
    to_learn.remove(RAND_WORD)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", mode="a", index=False)
    new_random_word()


def print_card():
    """Prints the new random word to the flash card. """
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_picture, image=front_image)
    canvas.itemconfig(text_title, text="French")
    canvas.itemconfig(text_word, text=f"{RAND_WORD['French']}")
    flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    """Flips the flash card so the other (English) side is visible."""
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_word, text=f"{RAND_WORD['English']}", fill="white")
    canvas.itemconfig(canvas_picture, image=back_image)


# Creating Window.

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Creating Img Files to be Used.
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
correct_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# Creating the Canvas.
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_picture = canvas.create_image(400, 263, image=front_image)
text_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "bold"))
text_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
# Creating Buttons.

correct_mark = Button(image=correct_image, highlightthickness=0, command=correct_guess)
correct_mark.grid(column=0, row=1)
wrong_mark = Button(image=wrong_image, highlightthickness=0, command=new_random_word)
wrong_mark.grid(column=1, row=1)
# Calling the Random Word Function To Print first Word. 
new_random_word()
window.mainloop()
