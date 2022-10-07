from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_choice)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_choice)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            if self.score > 6:
                self.canvas.itemconfig(self.question_text, text=f"Your score was {self.score * 10}% congrats, you pass!")
                self.true_button.config(state="disabled")
                self.false_button.config(state="disabled")

            elif self.score < 7:
                self.canvas.itemconfig(self.question_text, text=f"Your score was {self.score * 10}% you failed!!")
                self.true_button.config(state="disabled")
                self.false_button.config(state="disabled")
                
    def true_choice(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right=is_right)

    def false_choice(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right=is_right)

    def get_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green") 
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)