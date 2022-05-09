from tkinter import *

color = '#EB5353'
bg_color='#36AE7C'
fg_color = '#187498'



class Fader(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.time_allowed_for_sleep = 1 * 500
        self.n_words_typed = 0

    def fade_away(self, status):
        alpha = self.parent.attributes("-alpha")
        if status:
            alpha -= .1
            self.parent.attributes("-alpha", alpha)
            self.after(100, lambda: self.start_typing(event=self.type_txt))
        else:
            self.parent.attributes("-alpha", 1.0)
            self.after(100, lambda: self.start_typing(event=self.type_txt))

    def start_typing(self, event):
        self.type_txt.unbind('<Key>')
        self.typed_text_start = self.type_txt.get("1.0", END).strip()
        self.type_txt.after(self.time_allowed_for_sleep, lambda: self.check_results(st=self.typed_text_start))


    def check_results(self, st):
        self.txt_after_5sec = self.type_txt.get("1.0", END).strip()
        self.txt_5sec_list = [word for word in self.txt_after_5sec.split(" ")]
        self.n_words_typed =len(self.txt_5sec_list)
        self.n_words.configure(text= f'Number of Words Written: {self.n_words_typed}')

        if len(self.txt_after_5sec) <= len(st):
          return self.fade_away(status=True)
        else:
          print("False")
          return self.fade_away(status=False)


root = Tk()
fade= Fader(root)
fade.grid(column=0, row=0)

root.title("Ozan's Disappearing Text App")
root.minsize(width=400, height=400)
root.config(padx=20, pady=10, bg=color)


fade.msg = Label(text='Your text will gradually disappear when there is no typing.', font = ('Arial',30), fg=fg_color, bg=bg_color, padx=20)
fade.msg.grid(row=0, column=1, pady=20, padx=20)

fade.text_frame = Frame(width=800, height=250)
fade.text_frame.grid(row=1, column=1, pady=20)
#Freeze frame
fade.text_frame.grid_propagate(False)
fade.text_frame.columnconfigure(0, weight=1)
fade.type_txt = Text(fade.text_frame, font = ('Arial',15), padx=20)
fade.type_txt.focus()
fade.type_txt.grid(row=0, column=0)
fade.type_txt.grid_rowconfigure(0, weight=1)
fade.type_txt.grid_columnconfigure(0, weight=1)
fade.type_txt.bind('<Key>', fade.start_typing)
fade.n_words = Label(text=f'Number of words written: {fade.n_words_typed}', font = ('Arial',30), fg=fg_color, bg=bg_color, padx=20)
fade.n_words.grid(row=2, column=1, pady=20, padx=20)

root.mainloop()
