from tkinter import *
import time
import math
import random
user_words = []
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
COUNT_DOWN_SEC = 60
RESET = True
word_list = []
display = ""
user_words = []
wpm_count = 0
cpm_count = 0

with open("words.csv", encoding='utf-8') as file:
    for row in file:
        word_list.append(row.strip())


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global RESET, showed_words, user_words, wpm_count, cpm_count
    RESET = True
    showed_words = []
    user_words = []
    wpm_count = 0
    cpm_count = 0
    wpm_value.config(text=wpm_count)
    cpm_value.config(text=cpm_count)
    enter_words.config(state="disabled")
    canvas.itemconfig(timer_text, text=f"00")
    canvas.itemconfig(display_words, text="Use Spacebar between words.\n* Words are not case sensitive.\nPress Start button to begin.")





def start_timer():
    global RESET, showed_words, user_words, wpm_count, cpm_count
    if RESET == True:
        RESET = False
        global showed_words, user_words, wpm_count, cpm_count
        showed_words = []
        user_words = []
        wpm_count = 0
        cpm_count = 0
        wpm_value.config(text=wpm_count)
        cpm_value.config(text=cpm_count)
        enter_words.config(state="normal")
        random_words()
        countdown(60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global RESET
    if not RESET and count > 0:
        canvas.itemconfig(timer_text, text=f"{count}")
        window.after(1000, countdown, count - 1)
    if count == 0:
        compare()

def user_type(space):
    # Get the user written text
    user_words.append(enter_words.get("1.0", 'end-1c').title().strip())
    enter_words.delete('1.0', END)
    if len(user_words) % 8 == 0:
        random_words()


def random_words():
    global display
    display = ""
    for i in range(8):
        display_word = random.choice(word_list)
        showed_words.append(display_word)
        display += (display_word + ' ')
    canvas.itemconfig(display_words, text=display)
def compare():
    global wpm_count, cpm_count
    enter_words.config(state="disabled")
    for i in user_words:
        if i in showed_words:
            wpm_count += 1
            cpm_count += len(i)
    wpm_value.config(text=wpm_count)
    cpm_value.config(text=cpm_count)
    print(f"user_type: {user_words}")
    print(f"display_words: {showed_words}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Type Speed Counter")
window.config(padx=20, pady=20, bg=YELLOW)
# tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=500, height=500, bg=YELLOW, highlightthickness=0)
# canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(150, 40, text="00", fill="black", font=(FONT_NAME, 30, "bold"))
start_button = Button(text="Start", bg="white", command=start_timer)
start_button.grid(column=0, row=2)

restart_button = Button(text="Reset", bg="white", command=reset_timer)
restart_button.grid(column=0, row=3)

cpm_label = Label(text="Corrected CPM: ", bg=YELLOW,font=(FONT_NAME, 12, "bold"))
cpm_label.grid(row=0, column=0)
cpm_value = Label(text="?", bg=YELLOW, font=("FONT_NAME", 12,"bold"))
cpm_value.grid(row=0, column=0, columnspan=2)

wpm_label = Label(text="Words Per Minute: ", bg=YELLOW,font=(FONT_NAME, 12, "bold"))
wpm_label.grid(row=0, column=2)
wpm_value = Label(text="?", bg=YELLOW, font=("FONT_NAME", 12,"bold"))
wpm_value.grid(row=0, column=3)

timer = Label(window, text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW).place(x=250, y=-10)

enter_words= Text(window, width=20, height=3, state="disabled")
enter_words.grid(column=1, row=2)
canvas.create_image(400, 260)
display_words = canvas.create_text(150, 260, text="Use Spacebar between words.\n* Words are not case sensitive.\n Press Start button to begin.", font=("Arial", 14, "bold"), fill="black", justify="center", width=250)
canvas.grid(row=2, column=0, columnspan=2)
window.bind("<space>", user_type)
canvas.grid(column=1, row=1)
window.mainloop()
