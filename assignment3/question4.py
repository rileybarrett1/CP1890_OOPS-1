import tkinter as tk
from tkinter import ttk


def calculate():
    try:
        sidea = float(insertbox1.get())
        sideb = float(insertbox2.get())
        sidec = sidea * sideb
        answerbox.delete(0, tk.END)  # Clear previous result
        answerbox.insert(0, sidec)  # Insert new result
    except ValueError:
        answerbox.delete(0, tk.END)
        answerbox.insert(0, "Invalid Input")

# creating the window 
window = tk.Tk()
window.title("Right Triangle calculator")
window.geometry("250x150")
# creating the frame 
frame_form = ttk.Frame(window)
frame_form.pack(fill=tk.X, padx=10, pady=10)
# getting the labels in a row 
labels = ["Side A:", "Side B:", "Side C:"]
for i, label_text in enumerate(labels):
    label = ttk.Label(frame_form, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)
# making my insert boxes 
insertbox1 = ttk.Entry(frame_form)
insertbox1.grid(row=0, column=1, padx=5, pady=5)

insertbox2 = ttk.Entry(frame_form)
insertbox2.grid(row=1, column=1, padx=5, pady=5)

answerbox = ttk.Entry(frame_form)
answerbox.grid(row=2, column=1, padx=5, pady=5)
# creating the buttons 
button1 = ttk.Button(frame_form, text="Calculate", command=calculate)
button1.grid(row=3, column=0, pady=10)

button_exit = ttk.Button(frame_form, text="Exit", command=window.quit)
button_exit.grid(row=3, column=1, padx=5, pady=10)

window.mainloop()
