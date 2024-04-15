import csv
import sqlite3


def read_csv_to_db(db_file, csv_file, db_table):
    conn = sqlite3.connect(f'Question1_Supporting_Files/{db_file}')
    cursor = conn.cursor()
    query = f'drop table if exists Customer'
    cursor.execute(query)
    query = ("""CREATE TABLE Customer(
    customerID  INTEGER PRIMARY KEY     NOT NULL,
    firstName   TEXT                    NOT NULL,
    lastName    TEXT                    NOT NULL,
    companyName TEXT                    NULL,
    address     TEXT                    NULL,
    city        TEXT                    NULL,
    state       TEXT                    NULL,
    zip         TEXT                    NULL);""")
    cursor.execute(query)
    with open(f'Question1_Supporting_Files/{csv_file}', 'r', newline='') as n_file:
        reader = csv.reader(n_file, delimiter=',')
        next(reader)
        csv_list = list(reader)
        for row in csv_list:
            query = (f"INSERT INTO {db_table} "
                     f"values (NULL, '{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}');")
            cursor.execute(query)
        conn.commit()
        print("\nAll old rows deleted from Customer table")
        print(f'{len(csv_list)} row(s) inserted into {db_table} Table.')


def main():
    db_file = 'customers.sqlite'
    csv_file = 'customers.csv'
    db_table = 'customer'

    print("Customer Data Importer\n")
    print(f"CSV File:   {csv_file}")
    print(f"DB file:    {db_file}")
    print(f"Table name: {db_table}")
    read_csv_to_db(db_file, csv_file, db_table)


if __name__ == "__main__":
    main()

