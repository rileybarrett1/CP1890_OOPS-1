import sqlite3

conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, marks INTEGER);"""
print(query)
c.execute(query)
print("Table has been created")

c.execute("""INSERT into students VALUES (2, 'Arun Rameshbabu1', 30, 100)""")
conn.commit()
conn.close()

