import sqlite3

class Movie:
    def __init__(self, movie_title, movie_year):
        self.movie_title = movie_title
        self.movie_year = movie_year

    def __str__(self):
        return f"{self.movie_title} ({self.movie_year})"

class Categories:
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')  # Connect to SQLite database
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create a table to store movie titles and years
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                               (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)''')
        self.conn.commit()

    def add_movie(self, movie_title, movie_year):
        # Insert movie into the database
        self.cursor.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (movie_title, movie_year))
        self.conn.commit()

    def get_movies(self):
        # Retrieve all movies from the database
        self.cursor.execute("SELECT * FROM movies")
        return self.cursor.fetchall()

    def close_connection(self):
        # Close the database connection
        self.conn.close()

# Example usage:
categories = Categories()
categories.add_movie("Spirited Away", 2001)
categories.add_movie("The Lion King", 1994)

print("All Movies:")
for movie in categories.get_movies():
    print(movie)

categories.close_connection()
