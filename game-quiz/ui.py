from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Courier", 17, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Questions go here.", font=("Helvetica", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_photo_image = PhotoImage(file="images/true.png")
        self.true_button = Button( image=true_button_photo_image, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_button_photo_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_photo_image, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_q)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end")
            self.true_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.get_next_question(1000, self.get_next_question)


