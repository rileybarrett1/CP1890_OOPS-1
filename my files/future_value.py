import tkinter as tk
from tkinter import ttk,messagebox


# def calculate_future_value():
#     try:
#         principal = float(principal_entry.get())
#         rate = float(rate_entry.get())
#         time = float(time_entry.get())
#
#         future_value = principal * ((1 + rate / 100) ** time)
#
#         future_value_label.config(text=f"Future Value: ${future_value:.2f}")
#     except ValueError:
#         messagebox.showwarning("no data entered", "Please enter the data asked for ")
def clickedbutton1():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        future_value = 0
        future_value = principal * ((1 + rate / 100) ** time)

        future_value_label.config(text=f"Future Value: ${future_value:.2f}")
    except ValueError:
        messagebox.showwarning("no data entered", "Please enter the data asked for ")

# Create the main window
root = tk.Tk()
root.title("Future Value Calculator")

# Create and place labels and entries
principal_label = ttk.Label(root, text="Principal amount:")
principal_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
principal_entry = ttk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

rate_label = ttk.Label(root, text="Annual interest rate (%):")
rate_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
rate_entry = ttk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=5)

time_label = ttk.Label(root, text="Time period (years):")
time_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
time_entry = ttk.Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Create the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=clickedbutton1)
calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)

exit_button = ttk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=3, column=1, padx=10, pady=10)


# Create a label to display the future value
future_value_label = ttk.Label(root, text="")
future_value_label.grid(row=4, columnspan=2, padx=10, pady=5)

# Start the GUI main loop
root.mainloop()
