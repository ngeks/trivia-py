class Trivia:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.questions = questions
        self.current = None

    def get_new_question(self):
        import html
        self.current = self.questions[self.question_number]
        self.question_number += 1
        return html.unescape(self.current.question)

    def verify_answer(self, answer_given):
        correct_answer = self.current.answer

        if answer_given == correct_answer:
            self.score += 1
            return True
        else:
            return False
