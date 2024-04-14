import tkinter as tk
import tkinter.messagebox as ms
import re


def validate_date(P):
    # If the input is empty, allow it
    if not P:
        return True

    # Define a regular expression pattern for YYYY-MM-DD format
    pattern = r'^\d{0,4}-?\d{0,2}-?\d{0,2}$'

    # Check if the input matches the pattern
    if re.match(pattern, P):
        return True
    return False


def save_changes():
    if not all((entry1.get(), entry2.get(), entry3.get(), entry4.get())):
        ms.showerror("Blank Rows", "Please enter data in all fields.")
    elif not validate_date(entry1.get()):
        ms.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format.")
    else:
        ms.showinfo("Amount Updated", "Your amount was updated successfully.")

def get_amount():
    amount = entry3.get()
    if amount:
        ms.showinfo("Amount", f"Your current amount is: {amount}")
    else:
        ms.showinfo("Amount", "No amount entered yet.")

root = tk.Tk()
root.title("Edit Sales Amount")
root.geometry("350x200")

# Style for labels and entries
label_style = ("Arial", 12)
entry_style = ("Arial", 12)

# Date
label1 = tk.Label(root, text="Date:", font=label_style)
label1.grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(root, font=entry_style, validate="key")
entry1.grid(row=0, column=1)
# Set validation command to ensure date format
entry1['validatecommand'] = (root.register(validate_date), '%P')

# Region
label2 = tk.Label(root, text="Region:", font=label_style)
label2.grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(root, font=entry_style)
entry2.grid(row=1, column=1)

# Amount
label3 = tk.Label(root, text="Amount:", font=label_style)
label3.grid(row=2, column=0, sticky="w")
entry3 = tk.Entry(root, font=entry_style)
entry3.grid(row=2, column=1)

# ID
label4 = tk.Label(root, text="ID:", font=label_style)
label4.grid(row=3, column=0, sticky="w")
entry4 = tk.Entry(root, font=entry_style)
entry4.grid(row=3, column=1)

# Save Changes button
btn_save = tk.Button(root, text="Save Changes", command=save_changes)
btn_save.grid(row=4, column=1, pady=5, padx=10, sticky="sw")

# Exit button
btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.grid(row=4, column=1, pady=5, padx=10, sticky="se")

# Get Amount button
btn_get_amount = tk.Button(root, text="Get Amount", command=get_amount)
btn_get_amount.grid(row=0, column=2, rowspan=4, padx=5, pady=5, sticky="nsew")

root.mainloop()
