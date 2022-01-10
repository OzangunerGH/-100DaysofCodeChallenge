from tkinter import *


def button_clicked():
    new_text = round(int(input.get())*1.6)
    result_label.config(text=new_text)

#Creating the window.
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=150)
# Adding padding to window.
window.config(padx=20, pady=20, background="white")

# Creating input bar to let user enter the amount of miles.
input = Entry(width=10)
input.grid(column=1, row=0)

# Miles label.
miles = Label(text="miles", font=("Arial", 12, "bold"), background="white")
miles.grid(column=2, row=0)

## Is equal to label.
is_equal_to = Label(text="is equal to", font=("Arial", 12, "bold"), background="white")
is_equal_to.grid(column=0, row=1)

## Result Label (amount of KMs)
result_label = Label(text="0", font=("Arial", 14, "bold"), background="white")
result_label.grid(column=1, row=1)
# KM Label
km = Label(text="Km", font=("Arial", 12, "bold"), background="white")
km.grid(column=2, row=1)

# ( Calculate Button)
button = Button(text="Calculate", command=button_clicked, font=("Arial", 12, "bold"))
button.grid(column=1, row=2)

window.mainloop()

