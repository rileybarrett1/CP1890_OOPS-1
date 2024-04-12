class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def create_account(self, customer_name, initial_balance=0):
        if customer_name not in self.customers:
            self.customers[customer_name] = initial_balance
            print(f"Account created for {customer_name} with initial balance ${initial_balance}")
        else:
            print(f"Customer {customer_name} already has an account.")

    def deposit(self, customer_name, amount):
        if customer_name in self.customers:
            self.customers[customer_name] += amount
            print(f"${amount} deposited into {customer_name}'s account. New balance: ${self.customers[customer_name]}")
        else:
            print(f"Customer {customer_name} does not have an account.")

    def withdraw(self, customer_name, amount):
        if customer_name in self.customers:
            if self.customers[customer_name] >= amount:
                self.customers[customer_name] -= amount
                print(f"${amount} withdrawn from {customer_name}'s account. New balance: ${self.customers[customer_name]}")
            else:
                print(f"Insufficient funds in {customer_name}'s account.")
        else:
            print(f"Customer {customer_name} does not have an account.")

    def get_balance(self, customer_name):
        if customer_name in self.customers:
            print(f"Balance for {customer_name}: ${self.customers[customer_name]}")
        else:
            print(f"Customer {customer_name} does not have an account.")

# Example usage:
bank = Bank("MyBank")

bank.create_account("Alice", 100)
bank.create_account("Bob")

bank.deposit("Alice", 50)
bank.withdraw("Bob", 20)
bank.check_balance("Alice")
bank.check_balance("Bob")
