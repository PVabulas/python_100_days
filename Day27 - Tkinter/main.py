from tkinter import *


def button_clicked():
    try:
        miles = float(request.get())
        km = round(miles * 1.609344, 1)
        conversion.config(text=f"{km}")
    except ValueError:
        conversion.config(text="0")


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

l1 = Label(text="is equal to", font=("Arial", 12))
l2 = Label(text="Miles", font=("Arial", 12))
l3 = Label(text="Km", font=("Arial", 12))
button = Button(text="Calculate", command=button_clicked)
request = Entry(width=7)
conversion = Label(text="0", font=("Arial", 12))

l1.grid(column=1, row=2)
l1.config(padx=10, pady=5)
request.grid(column=2, row=1)
l1.config(padx=10, pady=5)
conversion.grid(column=2, row=2)
conversion.config(padx=10, pady=5)
button.grid(column=2, row=3)
button.config(padx=10, pady=5)
l2.grid(column=3, row=1)
l2.config(padx=10, pady=5)
l3.grid(column=3, row=2)
l3.config(padx=10, pady=5)

window.mainloop()
