from tkinter import *
from quiz_brain import QuizBrain
from data import get_questions
import html
from question_model import Question
from time import sleep

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


def answer_true():
    return True


def answer_false():
    return False


class QuizInterface(Tk):
    def __init__(self, question_bank):
        super().__init__()
        self.quiz = QuizBrain(question_bank)
        self.title("Quizzler")
        self.config(pady=20, padx=20, bg=THEME_COLOR)
        self.true_img = PhotoImage(file=f"images/true.png")
        self.false_img = PhotoImage(file=f"images/false.png")

        self.restart = Button(text="Start new quiz", command=self.reset_quiz)
        self.restart.grid(row=0, column=0)
        self.score = Label(bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)
        self.update_score()
        self.canvas = Canvas(width=400, height=300, bg="white")
        self.question_txt = self.canvas.create_text(
            200, 150, width=350, fill=THEME_COLOR, font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.next_question()
        self.true = Button(
            image=self.true_img,
            borderwidth=0,
            command=self.answer_true,
            highlightthickness=0,
        )
        self.true.grid(row=2, column=0)
        self.false = Button(
            image=self.false_img,
            borderwidth=0,
            command=self.answer_false,
            highlightthickness=0,
        )
        self.false.grid(row=2, column=1)

        self.mainloop()

    def next_question(self):
        self.quiz.next_question()
        self.canvas.itemconfig(self.question_txt, text=self.quiz.question)

    def update_score(self):
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def answer_true(self):
        is_correct = self.quiz.check_answer("True")
        self.flash_correct(is_correct)
        self.update_score()
        self.next_question()

    def answer_false(self):
        is_correct = self.quiz.check_answer("False")
        self.flash_correct(is_correct)
        self.update_score()
        self.next_question()

    def flash_correct(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.after(200, self.canvas.config, {"bg": "white"})

    def reset_quiz(self):
        question_bank = []
        question_data = get_questions()
        for question in question_data:
            question_text = html.unescape(question["question"])
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        self.quiz = QuizBrain(question_bank)
        self.update_score()
        self.next_question()
