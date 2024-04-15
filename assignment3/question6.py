import re
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect('sales.sqlite')
cur = conn.cursor()


def click_exit():
    esa_window.destroy()


def click_get_amount():
    date_format = re.compile("YYYY-MM-DD")
    region_format = re.compile("X")
    date = date_entry.get()
    region = region_entry.get()
    if date_format.match(date):
        if region_format.match(region):
            get_amount_db()
    else:
        messagebox.showwarning("Warning", "No data for date and region.")


def click_save():
    sale = amount_entry.get()
    sale = float(sale)
    query = f"update Sales set amount= '{sale}' where salesDate ={date_entry.get()} AND region = '{region_entry.get()}';"
    cur.execute(query)
    messagebox.showinfo("Info", "Saved successfully")


def get_amount_db():

    query = f"SELECT * FROM Sales WHERE salesDate = {date_entry.get()} AND region = '{region_entry.get()}';"
    sales = list(cur.execute(query))
    amount_var.set(sales[0][0])

# Window code ------------------------------------------
esa_window = tk.Tk()
esa_window.title("Edit Sales Amount")
esa_window.geometry("350x180")

esa_frame = ttk.Frame(esa_window, padding="10 10 10 10")
esa_frame.pack(fill="both", expand=True)

esa_info = ttk.Label(esa_frame, text="Enter date and region to get sales amount.")
esa_info.grid(column=0, row=0, columnspan=4, sticky=tk.N)

# date -------------------------------------------------

date_label = ttk.Label(esa_frame, text="Date:")
date_label.grid(column=0, row=1, sticky=tk.E)

date_var = tk.StringVar()
date_entry = ttk.Entry(esa_frame, textvariable=date_var, width=30)
date_entry.grid(column=1, row=1, columnspan=2, sticky=tk.W)

# region ----------------------------------------------

region_label = ttk.Label(esa_frame, text="Region:")
region_label.grid(column=0, row=2, sticky=tk.E)

region_var = tk.StringVar()
region_entry = ttk.Entry(esa_frame, textvariable=region_var, width=30)
region_entry.grid(column=1, row=2, columnspan=2, sticky=tk.W)

# amount ---------------------------------------------

amount_label = ttk.Label(esa_frame, text="Amount:")
amount_label.grid(column=0, row=3, sticky=tk.E)

amount_var = tk.StringVar()
amount_entry = ttk.Entry(esa_frame, textvariable=amount_var, width=30)
amount_entry.grid(column=1, row=3, columnspan=2, sticky=tk.W)

# ID --------------------------------------------------

id_label = ttk.Label(esa_frame, text="ID:")
id_label.grid(column=0, row=4, sticky=tk.E)

id_var = tk.StringVar()
id_entry = ttk.Entry(esa_frame, textvariable=id_var, width=30, state='readonly')
id_entry.grid(column=1, row=4, columnspan=2, sticky=tk.W)

# save button ----------------------------------------

save_button = ttk.Button(esa_frame, text="Save Changes", command=click_save)
save_button.grid(column=1, row=5, sticky=tk.W)


# exit button ----------------------------------------

exit_button = ttk.Button(esa_frame, text="Exit", command=click_exit)
exit_button.grid(column=2, row=5, sticky=tk.W)

# get amount button ------------------------------------------------------------------

get_button = ttk.Button(esa_frame, text="Get Amount", command=click_get_amount)
get_button.grid(column=3, row=2, sticky=tk.W)


for child in esa_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)
esa_window.mainloop()
