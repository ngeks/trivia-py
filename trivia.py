class Trivia:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def get_new_question(self):
        import html
        self.current_question = self.questions[self.question_number]
        self.question_number += 1
        return html.unescape(self.current_question.text)

    def is_answer_correct(self, answer_given):
        correct_answer = self.current_question.answer

        if answer_given == correct_answer:
            self.score += 1
            return True
        else:
            return False