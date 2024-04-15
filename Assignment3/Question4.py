# Question #4
import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt

window = tk.Tk()
window.title("Right Triangle Calculator")
window.geometry("330x130")
window.resizable(width=False, height=False)


def calculate():
    a = sideAText.get()
    b = sideBText.get()

    if not a.isnumeric():
        messagebox.showerror("Invalid Input", "Side A is not a valid integer.")
    elif not b.isnumeric():
        messagebox.showerror("Invalid Input", "Side B is not a valid integer.")
    else:
        if not int(a) > 0:
            messagebox.showerror("Invalid Input", "Side A must be positive.")
        elif not int(b) > 0:
            messagebox.showerror("Invalid Input", "Side B must be positive.")
        else:
            sideCText.set(f"{sqrt(int(a)**2 + int(b)**2):.3f}")


def exit_window():
    window.destroy()


frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

sideALabel = tk.Label(frame, text="Side A: ")
sideALabel.grid(column=0, row=0)
sideAText = tk.StringVar()
sideAEntry = tk.Entry(frame, width=40, textvariable=sideAText)
sideAEntry.grid(column=1, row=0, columnspan=2)

sideBLabel = tk.Label(frame, text="Side B: ")
sideBLabel.grid(column=0, row=1)
sideBText = tk.StringVar()
sideBEntry = tk.Entry(frame, width=40, textvariable=sideBText)
sideBEntry.grid(column=1, row=1, columnspan=2)

sideCLabel = tk.Label(frame, text="Side C: ")
sideCLabel.grid(column=0, row=2)
sideCText = tk.StringVar()
sideCEntry = tk.Entry(frame, width=40, textvariable=sideCText)
sideCEntry.grid(column=1, row=2, columnspan=2)
sideCEntry.config(state="readonly")

calculateButton = tk.Button(frame, width=9, text="Calculate", command=calculate)
calculateButton.grid(column=2, row=3, sticky=tk.W)

exitButton = tk.Button(frame, width=9, text="Exit", command=exit_window)
exitButton.grid(column=2, row=3, sticky=tk.E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

window.mainloop()
