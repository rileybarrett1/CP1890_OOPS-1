import sqlite3
from dataclasses import dataclass
import locale as lc
import csv
import datetime

lc.setlocale(lc.LC_ALL, "en_CA")
conn = sqlite3.connect('sales.sqlite')
cur = conn.cursor()


@dataclass
class DailySales:
    id: int
    amount: float
    saleData: str
    region: str

    def from_db(self):
        pass


@dataclass
class SalesList:
    sales: list

    def add(self, sale):
        self.sales.append(sale)


@dataclass
class Region:
    code: str
    name: str


@dataclass
class Regions:
    region_list: list

    def add(self):
        self.region_list.append(Region)


def view_sales():
    print(f"{'Date':<10}{'region':<10}{'amount':<10}")
    print("-"*35)
    sale_list = SalesList()
    query = "SELECT * FROM Sales ORDER BY date(saledate)"
    for sale in cur.execute(query):
        sale_list.add(DailySales(sale[0], sale[1], sale[2]))
    for i, n in enumerate(sale_list):
        print(f"{i}{n.saleDate:<10}{n.region:<10}{n.amount:<10}")


def import_sales():
    filename = input("file name: ")
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            query = f"INSERT INTO Sales VALUES (NULL, {row[1]}, {row[2]}, {row[3]})"
        conn.commit()


def add_sale():
    amount = float(input("Amount: "))
    date = datetime.date(input('Date: '))
    region = input('Region: ')
    query = f"INSERT INTO sales VALUES (NULL, {date}, {region}, {amount})"
    cur.execute(query)
    conn.commit()


def main():
    print("Stored Sales Importer")
    print("COMMAND MENU"
          "view    - View Sales List\n"
          "add     - Add Sales\n"
          "import  - Import Sales List\n"
          "exit    - Exit Program")

    while True:
        command = input("Command: ")

        if command == 'view':
            view_sales()
        elif command == 'add':
            add_sale()
        elif command == 'import':
            import_sales()
        elif command == 'exit':
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    main()