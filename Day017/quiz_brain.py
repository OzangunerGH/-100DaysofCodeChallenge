class QuizBrain:
"""Class QuizBrain can be used to ask questions, get answers and check if they are correct answers and provide user a score based on the number of correct answer."""
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0
        self.user_answer = ""

    def next_question(self):
      """ This method asks the user the question and gets his answer, then passes the user's answer to check_answer method."""
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}\nType True or False").capitalize()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
      """This method checks if there are any more questions left on the question list, and returns True or False."""
        return self.question_number < len(self.question_bank)

    def check_answer(self, user_answer, correct_answer):
      """This method checks if the answer user provided is the correct answer. If its correct, it adds 1 point to user's score."""
        if user_answer == correct_answer:
            self.score += 1
            print("You got the correct answer!")
        else:
            print("Sorry, that answer is incorrect.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Current Score:{self.score}/{self.question_number}")
        print("\n")
