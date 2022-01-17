from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
#Initializing the interface.
    def __init__(self, quiz_brain: QuizBrain):
        """This is a QuizInterface class to initiate the interface of the quiz program using Tkinter."""
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question Text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.correct_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=self.correct_image, highlightthickness=0, command=self.true_pressed)
        self.correct.grid(row=2, column=0, pady=20)

        self.false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false.grid(row=2, column=1, )

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """Prints next question to the screen if the quiz still has questions. Enables the answering buttons
        for the new question. Prints the updated score to the screen. If quiz has no more questions left,
        prints final score and tells the user the quiz is over."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.false.config(state="active")
            self.correct.config(state="active")
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.score_label.config(text=f"Score : {self.quiz.score}")

    def true_pressed(self):
        """Sets the user answer as True. Initiates the function to check whether the user answer was correct or wrong.
               Initiates the function to give feedback to user."""
        self.quiz.user_answer = "True"
        is_right = self.quiz.check_answer()
        self.give_feedback(is_right)

    def false_pressed(self):
        """Sets the user answer as False. Initiates the function to check whether the user answer was correct or wrong.
        Initiates the function to give feedback to user."""
        self.quiz.user_answer = "False"
        is_right = self.quiz.check_answer()
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Tells the user whether they got the answer correct or wrong.
        Disables the answering buttons to prevent answering a question multiple times.
        Initiates the next question function to move on with quiz."""
        self.false.config(state="disabled")
        self.correct.config(state="disabled")
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, func=self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, func=self.get_next_question)
