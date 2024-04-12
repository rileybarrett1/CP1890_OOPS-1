import sqlite3
from Database_class_excersize_objects import category, movie

DB_file = 'movies.sqlite'


def connect():
    conn = sqlite3.connect(DB_file)
    conn.row_factory = sqlite3.Row
    return conn


def connect():
    conn = sqlite3.connect(DB_file)
    row_factory = sqlite3.Row
    return conn


def close(conn):
    conn.close()
    print('Database closed')

def create_table(conn):
    cursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS categories (id integer PRIMARY KEY)"
