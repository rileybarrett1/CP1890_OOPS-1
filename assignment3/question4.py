import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt


def click_calc():
    a = A_entry.get()
    b = B_entry.get()
    if a == '' or b == '':
        messagebox.showerror('Error', 'Enter valid integer.')
    else:
        c = calc_c_value(a,b)
        C_str.set(f"{c:.3f}")


def calc_c_value(a_num, b_num):
    a = int(a_num)
    b = int(b_num)
    c = sqrt(a**2 + b**2)
    return float(c)


def click_exit():
    rtc_window.destroy()


# Window code --------------------------------------------------------------------------------------

rtc_window = tk.Tk()
rtc_window.title("Right Triangle Calculator")
rtc_window.geometry("320x150")

rtc_frame = ttk.Frame(rtc_window, padding='10 10 10 10')
rtc_frame.pack(fill='both', expand=True)

# side A box ---------------------------------------------------------------------------------------

A_label = ttk.Label(rtc_frame, text="Side A:")
A_label.grid(row=0, column=0)

A_integer = tk.IntVar()
A_entry = tk.Entry(rtc_frame, textvariable=A_integer, width=40)
A_entry.grid(row=0, column=1, columnspan=3)
A_entry.delete(0, tk.END)

# side B box ---------------------------------------------------------------------------------------

B_label = ttk.Label(rtc_frame, text="Side B:")
B_label.grid(row=1, column=0)

B_integer = tk.IntVar()
B_entry = tk.Entry(rtc_frame, textvariable=B_integer, width=40)
B_entry.grid(row=1, column=1, columnspan=3)
B_entry.delete(0, tk.END)

# side C box --------------------------------------------------------------------------------------

C_label = ttk.Label(rtc_frame, text="Side C:")
C_label.grid(row=2, column=0)

C_str = tk.StringVar()
C_entry = tk.Entry(rtc_frame, textvariable=C_str, width=40, state='readonly')
C_entry.grid(row=2, column=1, columnspan=3)
C_entry.delete(0, tk.END)

# calc button ----------------------------------------------------------------------------------------

calc_button = ttk.Button(rtc_frame, text="Calculate", command=click_calc)
calc_button.grid(row=3, column=2)

# exit button ----------------------------------------------------------------------------------------

exit_button = ttk.Button(rtc_frame, text="Exit", command=click_exit)
exit_button.grid(row=3, column=3)

# --------------------------------------------------------------------------------------------------------


for child in rtc_frame.winfo_children():
    child.grid_configure(padx=5, pady=3)
rtc_window.mainloop()
