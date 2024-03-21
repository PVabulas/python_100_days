from tkinter import *
from datetime import datetime, timedelta

# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
SEQUENCE = ["work", "short", "work", "short", "work", "short", "work", "long"]


class PomodoroWindow(Tk):
    periods = {
        1: {"title": "Work", "length": WORK_MIN, "checkmarks": ""},
        2: {"title": "Short Break", "length": SHORT_BREAK_MIN, "checkmarks": "✔"},
        3: {"title": "Work", "length": WORK_MIN, "checkmarks": "✔"},
        4: {"title": "Short Break", "length": SHORT_BREAK_MIN, "checkmarks": "✔✔"},
        5: {"title": "Work", "length": WORK_MIN, "checkmarks": "✔✔"},
        6: {"title": "Short Break", "length": SHORT_BREAK_MIN, "checkmarks": "✔✔✔"},
        7: {"title": "Work", "length": WORK_MIN, "checkmarks": "✔✔✔"},
        8: {"title": "Long Break", "length": LONG_BREAK_MIN, "checkmarks": "✔✔✔✔"},
    }

    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.config(padx=100, pady=50, bg=YELLOW)

        self.cur_time = datetime.min
        self.cur_period = 0
        self.checkmarks_var = StringVar()
        self.running = False

        self.canvas = Canvas(width=340, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(170, 112, image=self.tomato_img)
        self.timer_id = self.canvas.create_text(
            170, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
        )
        self.canvas.grid(column=2, row=2)

        self.title_label = Label(
            text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW
        )
        self.title_label.grid(column=2, row=1)
        self.start_btn = Button(text="Start", command=self.start_timer)
        self.start_btn.grid(column=1, row=3, sticky="E")
        self.pause_btn = Button(text="Pause", command=self.pause_timer)
        self.pause_btn.grid(column=2, row=3, pady=10)
        self.reset_btn = Button(text="Reset", command=self.reset_timer)
        self.reset_btn.grid(column=3, row=3, sticky="W")
        self.checkmarks_label = Label(
            textvariable=self.checkmarks_var,
            font=(FONT_NAME, 20, "bold"),
            fg=GREEN,
            bg=YELLOW,
        )
        self.checkmarks_label.grid(column=2, row=4)

        self.on_update()

    def on_update(self):
        # schedule timer to call myself after 1 second
        if self.running:
            if self.cur_time == datetime.min:
                self.next_period()
            else:
                self.cur_time -= timedelta(seconds=1)
            self.canvas.itemconfig(self.timer_id, text=f"{self.cur_time:%M:%S}")
        self.after(1000, self.on_update)

    def reset_timer(self):
        self.cur_time = datetime.min + timedelta(minutes=WORK_MIN)
        self.canvas.itemconfig(self.timer_id, text=f"{self.cur_time:%M:%S}")
        self.title_label.config(text=self.periods.get(1)["title"])
        self.cur_period = 1
        self.cur_time = datetime.min + timedelta(minutes=self.periods.get(1)["length"])
        self.checkmarks_var.set(self.periods.get(1)["checkmarks"])
        self.running = False

    def start_timer(self):
        self.running = True

    def pause_timer(self):
        self.running = False

    def next_period(self):
        period = self.cur_period + 1
        if self.periods.get(period):
            self.title_label.config(text=self.periods.get(period)["title"])
            self.cur_period = period
            self.cur_time = datetime.min + timedelta(
                minutes=self.periods.get(period)["length"]
            )
            self.checkmarks_var.set(self.periods.get(period)["checkmarks"])
        else:
            self.running = False
            self.cur_period = 0


window = PomodoroWindow()
window.mainloop()
