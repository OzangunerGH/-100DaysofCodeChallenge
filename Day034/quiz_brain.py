import html


class QuizBrain:

    def __init__(self, q_list):
        """This is a class to act as the brain of the quiz, which brings up next question, checks user answer,
        calculates score. """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.user_answer = None

    def still_has_questions(self):
        """This function checks if the quiz still has unanswered questions."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """This function returns the current question's text, so it can be displayed in the ui.
        Also keeps track of which question that the quiz is currently at."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self):
        """This function checks the user answer against the correct answer of the question,
        and returns True or False accordingly."""
        correct_answer = self.current_question.answer
        if self.user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
