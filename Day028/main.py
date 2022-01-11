from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg="pink")
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg="red")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Study", fg="green")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        start_timer()
        for _ in range(math.floor(reps / 2)):
            marks += "✓"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
reps = 0
timer = None





# Creating the UI Window and Canvas
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)

# Creating the Buttons,Texts and Labels
timer_text = canvas.create_text(110, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
button = Button(text="Start", bg="white", command=start_timer)
button.grid(column=0, row=2)
button = Button(text="Reset", bg="white", command=reset_timer)
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)
button.grid(column=2, row=2)
title_label = Label(text="Timer")
title_label.config(fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
window.mainloop()
