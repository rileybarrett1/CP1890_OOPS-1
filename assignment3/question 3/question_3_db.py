import sqlite3

conn = sqlite3.connect('Question3_Supporting_Files/task_list_db.sqlite')
cur = conn.cursor()


# all db function needed to interact with db

def view_tasks():
    query = "SELECT * FROM Task WHERE completed = 0"
    return list(cur.execute(query))


def view_hist():
    query = "SELECT * FROM Task WHERE completed = 1"
    return list(cur.execute(query))


def add_task(description):
    query = f"INSERT INTO Task VALUES (NULL, '{description}', 0)"
    cur.execute(query)
    conn.commit()


def comp_task(description):
    query = f"UPDATE Task SET completed = 1 WHERE description = '{description}'"
    cur.execute(query)
    conn.commit()


def del_task(description):
    query = f"DELETE FROM Task WHERE description = '{description}'"
    cur.execute(query)
    conn.commit()
