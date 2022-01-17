# This is an updated version of Quiz Program that I did at Day 17. Compared to the old one,
# the new one is now displayed with a User Interface instead of command line, you can answer by pressing buttons.
# instead of typing your answers in. And the questions are gathered by API, which makes the program show up
# different set of questions each time it is executed.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
# Passing Question Objects to the question_bank list.
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creating QuizBrain and QuizInterface objects.
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

