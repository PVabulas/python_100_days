from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


class PasswordManager(Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.config(padx=50, pady=50)
        self.logo_canvas = Canvas(height=200, width=200)
        self.logo = PhotoImage(file="logo.png")
        self.logo_canvas.create_image(100, 100, image=self.logo)
        self.logo_canvas.grid(column=1, row=0)

        self.labels = {
            "website": {
                "label": Label(text="Website:"),
                "entry": Entry(width=27),
                "row": 1,
            },
            "username": {
                "label": Label(text="Email/Username:"),
                "entry": Entry(width=48),
                "row": 2,
                "colspan": 2,
            },
            "password": {
                "label": Label(text="Password:"),
                "entry": Entry(width=27),
                "row": 3,
            },
        }
        for info in self.labels.values():
            info["label"].grid(column=0, row=info["row"])
            info["entry"].grid(
                column=1, row=info["row"], columnspan=info.get("colspan", 1), sticky="w"
            )
        search_button = Button(text="Search", command=self.find_password)
        search_button.grid(column=2, row=1, sticky="we")
        generate_password_button = Button(
            text="Generate Password", command=self.generate_password
        )
        generate_password_button.grid(column=2, row=3)
        add_button = Button(text="Add", width=36, command=self.add_password)
        add_button.grid(column=1, row=4, columnspan=2)

        self.labels["website"]["entry"].focus()

    def add_password(self):
        website = self.labels["website"]["entry"].get()
        username = self.labels["username"]["entry"].get()
        password = self.labels["password"]["entry"].get()
        for entry in self.labels.values():
            entry["entry"].delete(0, END)

        is_ok = all([len(entry) > 0 for entry in [website, username, password]])
        if not is_ok:
            messagebox.showerror(
                title=f"Missing information", message=f"Missing information"
            )
        else:
            is_ok = messagebox.askyesno(
                title=website,
                message=f"These are the details entered: \nUsername: {username}\nPassword: {password}\nIs it ok to save?",
            )

        if is_ok:
            out = {website: {"username": username, "password": password}}
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
                    data.update(out)
            except FileNotFoundError:
                data = out
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        pyperclip.copy(password)
        self.labels["website"]["entry"].focus()

    def generate_password(self):
        password = generate_password()
        self.labels["password"]["entry"].delete(0, END)
        self.labels["password"]["entry"].insert(0, password)
        pyperclip.copy(password)

    def find_password(self):
        try:
            with open("data.json") as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror(
                title=f"No existing data file", message=f"No existing data file"
            )
            return

        website = self.labels["website"]["entry"].get()

        if website in data:
            username = data[website].get("username", "")
            self.labels["username"]["entry"].delete(0, END)
            self.labels["username"]["entry"].insert(0, username)
            password = data[website].get("password", "")
            self.labels["password"]["entry"].delete(0, END)
            self.labels["password"]["entry"].insert(0, password)
            pyperclip.copy(password)
        else:
            messagebox.showerror(
                title=f"Missing password", message=f"No password held for this website"
            )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

pm = PasswordManager()
pm.mainloop()
