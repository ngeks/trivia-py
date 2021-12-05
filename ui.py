from tkinter import *
from trivia import Trivia

# colors
BACKGROUND = "#214F4B"
BG_WHITE = "#F8F7F9"
BG_CORRECT = "#78BC61"
BG_WRONG = "#E9806E"

# font styles
SCORE_FONT = ("Verdana", 9, "bold")
CANVAS_FONT = ("Verdana", 15, "italic")

# window title
TITLE = "Trivia Py - steezyouthere"


class UI(Tk):
    def __init__(self, trivia: Trivia):
        super().__init__()
        self.trivia = trivia

        self.config(padx=20, pady=20, bg=BACKGROUND)
        self.title(TITLE)

        self.score = Label(text=f"Score: {self.trivia.score}/{len(self.trivia.questions)}", fg="white", bg=BACKGROUND, font=SCORE_FONT)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg=BG_WHITE)
        self.canvas_text = self.canvas.create_text(150, 125, text="", width=280, font=CANVAS_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(40, 40))

        true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_img, bd=0, command=self.true_btn_pressed)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_img, bd=0, command=self.false_btn_pressed)
        self.false_btn.grid(row=2, column=1)

        self.display_new_question()

        self.mainloop()

    def display_new_question(self):
        """Display a new question."""
        self.canvas.config(bg=BG_WHITE)
        if self.trivia.question_number < len(self.trivia.questions):
            question = self.trivia.get_new_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the trivia questions.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def is_answer_correct(self, is_correct):
        """Check if answer is correct. If yes, display new question."""
        if is_correct:
            self.canvas.config(bg=BG_CORRECT)
            self.score.config(text=f"Score: {self.trivia.score}/{len(self.trivia.questions)}")
        else:
            self.canvas.config(bg=BG_WRONG)
        self.after(1000, self.display_new_question)

    def true_btn_pressed(self):
        """Verify if TRUE is the correct answer."""
        self.is_answer_correct(self.trivia.verify_answer("True"))

    def false_btn_pressed(self):
        """Verify if FALSE is the correct answer."""
        self.is_answer_correct(self.trivia.verify_answer("False"))
