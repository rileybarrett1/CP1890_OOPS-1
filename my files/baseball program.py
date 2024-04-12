from datetime import datetime
import tkinter as tk
from tkinter import ttk


# def menu():
#     while True:
#         print(25 * "=")
#         print("  baseball Team Manager  ")
#         date_time_now=datetime.now()
#         print(date_time_now)
#         print("days until game: 2")
#
#         print("MENU OPTIONS")
#         print("1 - display lineup \n2 - add player \n3 - remove player \n4 - move player \n5 - edit player position \n6 - edit player stats \n7 - exit program")
#         player_lineup = [["tommy la stella", "3b", 1316, 360, 0.274],
#                          ["mike yastrzmski", "rf", 563, 168, 0.281],
#                          ["donavan solano", "2b", 1473, 407, 0.276],
#                          ["Buster posey", "c", 5473, 1380, 0.302],
#                          ["Brandon belt", "1b", 3811, 1003, 0.263],
#                          ["Brandon crawford", "ss", 4402, 1099, 0.250],
#                          ["alex dickerson", "Lf", 586, 160, 0.273],
#                          ["austin slater", "CF", 569, 147, 0.274],
#                          ["kein gausman", "P", 56, 2, 0.036]]
#         positions = ["c", "1b", "2b", "3b", "ss", "lf", "cf", "rf", "f"]


def add_player(player_lineup):
    player_name = input("player name: ")
    player_position = input("player pos: ")
    player_average_bat = input("avg bats: ")
    player_hits = input("player hits: ")
    player_avg = input("player avg hits: ")
    player_lineup.append(player_name, player_position, player_average_bat, player_hits, player_hits)


def drop_player(player_lineup):
    drop_player = input("enter player number :")
    player_lineup.remove(drop_player)


# def main(player_lineup,positions):
#     while True:
#         menu_choice = int(input("menu options: "))
#         if menu_choice == 1:
#             print(f"{player_lineup}\n{positions}")
#         if menu_choice == 2:
#             add_player()
#         if menu_choice == 3:
#             drop_player()



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
first_window.title("Player")
first_window.geometry("425x375")

frame = ttk.Frame(first_window, padding="10")
frame.pack(fill="both", expand=True)

id_p = ttk.Label(frame, text="player id:")
id_p.grid(column=0, row=0, sticky="w")

first_name_label = ttk.Label(frame, text="first name:")
first_name_label.grid(column=0, row=1, sticky="w")


last_name = ttk.Label(frame, text="last name:")
last_name.grid(column=0, row=2, sticky="w")

position = ttk.Label(frame, text="position:")
position.grid(column=0, row=3, sticky="w")

all_bats = ttk.Label(frame, text="bats:")
all_bats.grid(column=0, row=4, sticky="w")

bat_avg = ttk.Label(frame, text="batting avg:")
bat_avg.grid(column=0, row=5, sticky="w")

name_text = tk.StringVar()
name_entry = ttk.Entry(frame, width=30, textvariable=name_text, foreground="grey")
name_entry.insert(0, "Enter your player id...")
name_entry.bind("<FocusIn>", on_entry_click)
name_entry.bind("<FocusOut>", on_focusout)
name_entry.grid(column=1, row=0, padx=(0, 10), sticky="we")



first_name_label = tk.StringVar()
first_name_label = ttk.Entry(frame, width=30, textvariable=first_name_label, foreground="grey")
first_name_label.insert(0, "Enter your first name")
first_name_label.grid(column=1, row=1, padx=(0, 10), sticky="we")

# first_name = tk.StringVar()
# first_name_entry = ttk.Entry(frame, width=30, textvariable=first_name,  foreground="grey")
# first_name_entry.insert(0,"enter your first name...")
# first_name_entry.grid(column=1, row=2, padx=(0, 10), sticky="we")

last_name = tk.StringVar()
last_name_entry = ttk.Entry(frame, width=30, textvariable=last_name,  foreground="grey")
last_name_entry.insert(0,"enter your last name...")
last_name_entry.grid(column=1, row=2, padx=(0, 10), sticky="we")

position = tk.StringVar()
position_entry = ttk.Entry(frame, width=30, textvariable=position,  foreground="grey")
position_entry.insert(0,"enter your position...")
position_entry.grid(column=1, row=3, padx=(0, 10), sticky="we")

all_bats = tk.StringVar()
all_bats_entry = ttk.Entry(frame, width=30, textvariable=all_bats,  foreground="grey")
all_bats_entry .insert(0,"enter your bats...")
all_bats_entry.grid(column=1, row=4, padx=(0, 10), sticky="we")


bat_avg= tk.StringVar()
bat_avg_entry = ttk.Entry(frame, width=30, textvariable=bat_avg,  foreground="grey")
bat_avg_entry.insert(0,"enter your batting avg...")
bat_avg_entry.grid(column=1, row=5, padx=(0, 10), sticky="we")

button1 = ttk.Button(frame, text="Save Changes", command=clicked_button1)
button2 = ttk.Button(frame, text="Cancel", command=clicked_button2)
button1.grid(column=1, row=6, pady=(10, 0), sticky="w")
button2.grid(column=1, row=6, pady=(10, 0), sticky="e")

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

first_window.mainloop()



