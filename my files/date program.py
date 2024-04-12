from datetime import datetime

def main():
    while True:
        print("The Invoice Due Date Program")
        invoice = input("Enter Invoice Due Date(YYYY-MM-DD): ")

        due_date = datetime.strptime(invoice, "2/14/2021")
        current_date = datetime.now()
        invoice_date = datetime.strptime(invoice, "1/14/2021")

        due_date2 = current_date - due_date

        print(f"your due_date is {due_date2} overdue")

        cont=input("continue? (y/n): ")
        if cont != "y" or cont != "Y":
            break

if __name__ == "__main__":
    main()