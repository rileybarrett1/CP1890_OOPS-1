import csv
import sqlite3


def create_customer_table(db_file):
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()

            # Create the Customer table if it does not exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
                                id INTEGER PRIMARY KEY,
                                firstName TEXT,
                                lastName TEXT,
                                companyName TEXT,
                                address TEXT,
                                city TEXT,
                                state TEXT,
                                zip TEXT
                              );''')

    except sqlite3.Error as error:
        print("Error creating Customer table:", error)


def import_customers_from_csv(csv_file, db_file):
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()

            # Delete old data from Customer table
            cursor.execute("DELETE FROM Customer")

            # Read data from CSV and insert into the Customer table using executemany
            with open(csv_file, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header row
                rows = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in csv_reader]
                cursor.executemany(
                    "INSERT INTO Customer (firstName, lastName, companyName, address, city, state, zip) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    rows)
        print("all old rows deleted from customer table ")
        print("500 rows inserted into customer table")

    except sqlite3.Error as error:
        print("Error while importing customers:", error)


def table():
    print("Customer data importer")
    print(f"Db file: Customers.csv")
    print(f"Db file: Customers.db")
    print()


# Replace these values with your file paths
csv_file = 'customers.csv'
db_file = 'customers.db'

create_customer_table(db_file)
table()
import_customers_from_csv(csv_file, db_file)
