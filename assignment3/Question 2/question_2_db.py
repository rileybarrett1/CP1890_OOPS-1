import sqlite3

conn = sqlite3.connect("Question2_Supporting_Files/player_db.sqlite")
cur = conn.cursor()


# creating all action need for db access.
def select_all():
    query = "SELECT * FROM player ORDER BY wins DESC"
    return list(cur.execute(query))


def add_player(name, wins, losses, ties):
    query = f"INSERT INTO Player VALUES (NULL, '{name}', '{wins}', '{losses}', '{ties}')"
    cur.execute(query)
    conn.commit()


def update_player(name, wins, losses, ties):
    query = f"UPDATE Player SET wins = {wins}, losses = {losses} , ties = {ties} WHERE name = '{name}';"
    cur.execute(query)
    conn.commit()


def delete_player(name):
    query = f"DELETE FROM Player WHERE name = '{name}'"
    cur.execute(query)
    conn.commit()
