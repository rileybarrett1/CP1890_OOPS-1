import tkinter as tk
from tkinter import ttk

def clicked_button1():
    first_window.title("Yes!, I am the cool button")
    name = name_text.get()
    about_text.set(f"{name} is cool")

def clicked_button2():
    first_window.destroy()

def on_entry_click(event):
    """Function to clear the entry widget when clicked."""
    if name_entry.get() == "Enter your name...":
        name_entry.delete(0, "end")
        name_entry.insert(0, "")
        name_entry.config(fg="black")

def on_focusout(event):
    """Function to replace placeholder text when focus is lost."""
    if name_entry.get() == "":
        name_entry.insert(0, "Enter your name...")
        name_entry.config(fg="grey")

# creating empty window
first_window = tk.Tk()
first_window.title("My First GUI")
first_window.geometry("400x150")

frame = ttk.Frame(first_window, padding="10")
frame.pack(fill="both", expand=True)

name_label = ttk.Label(frame, text="Name:")
name_label.grid(column=0, row=0, sticky="w")

name_text = tk.StringVar()
name_entry = ttk.Entry(frame, width=30, textvariable=name_text, foreground="grey")
name_entry.insert(0, "Enter your name...")
name_entry.bind("<FocusIn>", on_entry_click)
name_entry.bind("<FocusOut>", on_focusout)
name_entry.grid(column=1, row=0, padx=(0, 10), sticky="we")

about_Label = ttk.Label(frame, text="About:")
about_Label.grid(column=0, row=1, sticky="w")

about_text = tk.StringVar()
about_entry = ttk.Entry(frame, width=30, textvariable=about_text, state="readonly")
about_entry.grid(column=1, row=1, padx=(0, 10), sticky="we")

button1 = ttk.Button(frame, text="I'm cool", command=clicked_button1)
button2 = ttk.Button(frame, text="No, I'm cool", command=clicked_button2)
button1.grid(column=0, row=2, pady=(10, 0), sticky="we")
button2.grid(column=1, row=2, pady=(10, 0), sticky="we")

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

first_window.mainloop()
