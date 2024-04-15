# Question #6
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("SupportingFiles/Question5/Q5Database.sqlite")
c = conn.cursor()

window = tk.Tk()
window.title("Edit Sales Amount")
window.geometry("330x190")
window.resizable(width=False, height=False)


def get_amount():
    try:
        sale = list(c.execute(f"""SELECT * FROM Sales WHERE salesDate = "{dateEntry.get()}" AND region = "{regionEntry.get()}" LIMIT 1;"""))
        amountText.set(sale[0][1])
        idText.set(sale[0][0])
    except IndexError:
        messagebox.showerror("Invalid Input", "No sale found.")


def save_changes():
    value = amountText.get()

    try:
        value = float(value)
        c.execute(f"""UPDATE Sales SET amount = {value} WHERE salesDate = "{dateEntry.get()}" AND region = "{regionEntry.get()}";""")

    except ValueError:
        messagebox.showerror("Invalid Input", "Amount is not a valid integer.")


def exit_window():
    window.destroy()


frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

dateLabel = tk.Label(frame, text="Enter date and region to get sales amount.")
dateLabel.grid(column=0, row=0, columnspan=3)

dateLabel = tk.Label(frame, text="Date: ")
dateLabel.grid(column=0, row=1, sticky=tk.E)
dateText = tk.StringVar()
dateEntry = tk.Entry(frame, width=23, textvariable=dateText)
dateEntry.grid(column=1, row=1)

regionLabel = tk.Label(frame, text="Region: ")
regionLabel.grid(column=0, row=2, sticky=tk.E)
regionText = tk.StringVar()
regionEntry = tk.Entry(frame, width=23, textvariable=regionText)
regionEntry.grid(column=1, row=2)

amountLabel = tk.Label(frame, text="Amount: ")
amountLabel.grid(column=0, row=3, sticky=tk.E)
amountText = tk.StringVar()
amountEntry = tk.Entry(frame, width=23, textvariable=amountText)
amountEntry.grid(column=1, row=3)

idLabel = tk.Label(frame, text="ID: ")
idLabel.grid(column=0, row=4, sticky=tk.E)
idText = tk.StringVar()
idEntry = tk.Entry(frame, width=23, textvariable=idText)
idEntry.grid(column=1, row=4)
idEntry.config(state="readonly")

getAmountButton = tk.Button(frame, width=11, text="Get Amount", command=get_amount)
getAmountButton.grid(column=2, row=2)

calculateButton = tk.Button(frame, width=11, text="Save Changes", command=save_changes)
calculateButton.grid(column=1, row=5, sticky=tk.W)

exitButton = tk.Button(frame, width=6, text="Exit", command=exit_window)
exitButton.grid(column=1, row=5, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

window.mainloop()
