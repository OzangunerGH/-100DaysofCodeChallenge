#Creating a class  from the list of questions named Question and passing the attributes text and answer.
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
