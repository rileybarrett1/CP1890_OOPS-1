# Question #5
import datetime, csv, sqlite3
import locale as lc
from dataclasses import dataclass

lc.setlocale(lc.LC_ALL, "en_CA")
conn = sqlite3.connect("SupportingFiles/Question5/Q5Database.sqlite")
c = conn.cursor()


@dataclass
class Region:
    code: str
    name: str


@dataclass
class Regions:
    regions: list

    def __init__(self):
        self.regions = []
        for region in c.execute("""SELECT * FROM Region"""):
            self.add(Region(region[0], region[1]))

    def add(self, region):
        self.regions.append(region)


@dataclass
class DailySales:
    id: int
    amount: float
    salesDate: str
    region: str
    quarter: int

    def fromDb(self):
        pass


@dataclass
class SalesList:
    sales: list

    def __init__(self):
        self.sales = []

    def add(self, sale):
        self.sales.append(sale)


class Db:
    @staticmethod
    def get_all_sales() -> SalesList:
        salesList = SalesList()
        for sale in c.execute("""SELECT * FROM Sales ORDER BY DATE(salesDate)"""):
            salesList.add(DailySales(sale[0], sale[1], sale[2], sale[3], int(sale[2].split('-')[1])//4+1))
        return salesList

    @staticmethod
    def add(amount: float, date: str, region: str) -> None:
        c.execute(f"""INSERT INTO Sales VALUES (NULL, {amount}, "{date}", "{region}");""")
        conn.commit()

    @staticmethod
    def import_csv(fileName: str) -> None:
        with open(fileName) as csvFile:
            file = csv.reader(csvFile, delimiter=',')
            next(file)  # Skips Header
            for line in file:
                c.execute(f"""INSERT INTO Sales VALUES (NULL, {line[1]}, "{line[2]}", "{line[3]}");""")
            conn.commit()


def get_float(prompt: str) -> float:
    while True:
        response = input(prompt)
        if response.isnumeric():
            return float(response)
        print("Invalid input. Please try again.\n")


def get_date(prompt: str) -> str:
    while True:
        response = input(prompt)
        try:
            datetime.date.fromisoformat(response)
            return response
        except ValueError:
            print("Invalid input. Please try again.\n")


def view():
    total = 0
    print(f"{'Date':>9}{'Quarter':>18}{'Region':>14}{'Amount':>19}")
    print(60 * '-')
    for n, data in enumerate(Db.get_all_sales().sales, 1):
        print(f"{f'{n}.':<5}{data.salesDate:<15}{data.quarter:<15}{data.region:6}{lc.currency(data.amount, grouping=True):>19}")
        total += int(data.amount)
    print(60 * '-')
    print(f"TOTAL:{lc.currency(total, grouping=True): >54}")


def add():
    amount = get_float("Amount: ")
    date = get_date("Date(YYYY-MM-DD): ")
    region = input("Region: ")
    Db.add(amount, date, region)


def import_file():
    fileName = input("File name: ")
    Db.import_csv(fileName)


def menu():
    print("\n"
          "COMMAND MENU\n"
          "view   - View all sales\n"
          "add    - Add sales\n"
          "import - Import sales from file\n"
          "menu   - Show menu\n"
          "exit   - Exit program")


def main():
    print("SALES DATA IMPORTER")
    menu()

    while True:
        command = input("\nPlease enter a command: ").lower()

        if command == "view":
            view()
        elif command == "add":
            add()
        elif command == "import":
            import_file()
        elif command == "menu":
            menu()
        elif command == "exit":
            print("\nBye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
