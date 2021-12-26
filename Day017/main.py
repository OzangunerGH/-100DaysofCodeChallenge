from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
#Importing classes and question data.


# Getting the question text and answer and creating a Question object from each pair of question text and question answers, 
# then passing those question objects in question_bank list variable.

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

#Creating the quiz object from QuizBrain class and using necessary methods to start the game

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
