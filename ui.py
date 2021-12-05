from tkinter import *

# colors
BACKGROUND = "#214F4B"
BG_WHITE = "#F8F7F9"

# font styles
SCORE_FONT = ("Verdana", 9, "bold")
CANVAS_FONT = ("Verdana", 15, "italic")

# window title
TITLE = "Trivia Py - steezyouthere"


class UI(Tk):
    def __init__(self):
        super().__init__()
        self.config(padx=20, pady=20, bg=BACKGROUND)
        self.title(TITLE)

        self.score = Label(text="Score: 0", fg="white", bg=BACKGROUND, font=SCORE_FONT)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg=BG_WHITE)
        self.canvas_text = self.canvas.create_text(150, 125, text="", width=280, font=CANVAS_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(40, 40))

        true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_img, bd=0)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_img, bd=0)
        self.false_btn.grid(row=2, column=1)

        self.mainloop()
        