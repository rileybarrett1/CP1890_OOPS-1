# Question #1
import csv
import sqlite3


def main():
    # Constants, since the console example and specifications don't seem to imply
    #  that they're user inputs
    csv_file = 'customers.csv'
    db_file = 'customers.sqlite'
    table = 'Customer'

    print("Customer Data Importer\n")
    print(f"CSV file:   {csv_file}")
    print(f"DB file:    {db_file}")
    print(f"Table name: {table}")

    conn = sqlite3.connect(f"SupportingFiles/Question1/{db_file}")
    c = conn.cursor()

    c.execute("""DROP TABLE IF EXISTS Customer;""")
    print("\nAll old row(s) deleted from Customer table.")

    c.execute("""CREATE TABLE Customer(
                    customerID  INTEGER PRIMARY KEY    NOT NULL,
                    firstName   TEXT                   NOT NULL,
                    lastName    TEXT                   NOT NULL,
                    companyName TEXT                   NULL,
                    address     TEXT                   NULL,
                    city        TEXT                   NULL,
                    state       TEXT                   NULL,
                    zip         TEXT                   NULL);""")

    with open(f"SupportingFiles/Question1/{csv_file}", newline='') as csvFile:
        file = csv.reader(csvFile, delimiter=',')
        next(file)  # Skips Header
        file = list(file)
        for line in file:
            query = f"""INSERT INTO Customer VALUES (NULL, "{line[0]}", "{line[1]}", "{line[2]}", "{line[3]}", "{line[4]}", "{line[5]}", "{line[6]}");"""
            c.execute(query)
        conn.commit()
        print(f"{len(file)} row(s) inserted into Customer table.")


if __name__ == "__main__":
    main()
