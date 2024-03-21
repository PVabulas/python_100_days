from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"


class Flashcards(Tk):
    def __init__(self, data_file=None):
        super().__init__()
        self.front_word = ""
        self.back_word = ""
        self.flip_id = None
        try:
            df = pd.read_csv(
                "../Archive/Day31 - Flashcards/data/words_to_learn.csv", index_col=0
            )
        except FileNotFoundError:
            if data_file is None:
                raise FileNotFoundError(
                    "Must provide data_file if no existing words to learn."
                )
            df = pd.read_csv(data_file, index_col=0)
        self.words = df[df.columns[0]].to_dict()
        self.front_title = df.index.name
        self.back_title = df.columns[0]
        self.title("Flashy")
        self.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
        self.front = PhotoImage(
            file="../Archive/Day31 - Flashcards/images/card_front.png"
        )
        self.back = PhotoImage(
            file="../Archive/Day31 - Flashcards/images/card_back.png"
        )
        self.right = PhotoImage(file="../Archive/Day31 - Flashcards/images/right.png")
        self.wrong = PhotoImage(file="../Archive/Day31 - Flashcards/images/wrong.png")
        self.canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
        self.flashcard = self.canvas.create_image(400, 263)
        self.card_title = self.canvas.create_text(
            400, 150, font=("Ariel", 40, "italic")
        )
        self.word = self.canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
        self.new_flashcard()
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.right_button = Button(
            image=self.right, borderwidth=0, command=self.correct_answer
        )
        self.right_button.grid(
            row=1,
            column=0,
        )
        self.wrong_button = Button(
            image=self.wrong, borderwidth=0, command=self.new_flashcard
        )
        self.wrong_button.grid(row=1, column=1)

    def get_new_word(self):
        self.front_word, self.back_word = choice(list(self.words.items()))

    def new_flashcard(self):
        if self.flip_id:
            self.after_cancel(self.flip_id)
        self.get_new_word()
        self.after(0, self.show_front)
        self.flip_id = self.after(3000, self.flip_card)

    def show_front(self):
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.word, text=self.front_word, fill="black")
        self.canvas.itemconfig(self.flashcard, image=self.front)

    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.word, text=self.back_word, fill="white")
        self.canvas.itemconfig(self.flashcard, image=self.back)

    def correct_answer(self):
        del self.words[self.front_word]
        out = pd.Series(self.words)
        out.to_csv(
            "data/words_to_learn.csv",
            index_label=self.front_title,
            header=[self.back_title],
        )
        self.new_flashcard()


if __name__ == "__main__":
    data = "data/french_words.csv"
    flashcards = Flashcards(data)
    flashcards.mainloop()
