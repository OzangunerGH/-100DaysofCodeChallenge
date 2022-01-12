# Importing necessary libraries and methods.

import random
from tkinter import *
from tkinter import messagebox
import pyperclip


# Function to generate random password.

def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.delete(0, END)
    pyperclip.copy(password)
    return password_entry.insert(0, password)


# Function to add entry to data.txt file when Add button is pressed.
def add_entry():
    email = e_mail_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="The fields email, website, password can not be empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Are details {email} {password} correct?"
                                                                     f"\n Press OK to Save.")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} |{password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Creating the Window.
window = Tk()
window.title("Random Password Generator / Saver")
window.config(padx=20, pady=20)
bg_picture = PhotoImage(file="logo.png")
# Creating the Canvas.
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bg_picture)
canvas.grid(column=1, row=0)

# Creating Labels and Entry Fields.
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

e_mail_label = Label(text="E-mail/Username:")
e_mail_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

website_entry.focus()

e_mail_entry = Entry(width=35)
e_mail_entry.insert(END, string="example@email.com")
e_mail_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

# Creating Buttons.

generate_password = Button(text="Generate Password", bg="white", command=random_password)
generate_password.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, bg="white", command=add_entry)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
