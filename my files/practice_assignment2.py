import random

class List(list):
    def __init__(self):
        random_list = []


class Randomintlist(list):
    def __init__(self, n):
        if not (0 < n <= 100):
            raise ValueError("Please enter an integer between 1 and 100")
        super().__init__(random.randint(0, 100) for _ in range(n))

    def total_int(self):
        return sum(self)

    def count_average(self):
        return sum(self) / len(self)

    def __str__(self):
        return ", ".join(map(str, self))


while True:
    print("Random integer list")
    try:
        n = int(input("How many random integers should the list contain?: "))
        if 0 < n <= 100:
            random_list = Randomintlist(n)
            print(f"The random integers are: {random_list}")
            print(f"The count is: {len(random_list)}")
            print(f"The total is: {random_list.total_int()}")
            print(f"The average is: {random_list.count_average():.2f}")
        else:
            print("Please enter an integer between 1 and 100")
    except ValueError:
        print("Invalid input. Please enter a valid integer")

    choice = input("Do you want to continue? (y/n): ").lower()
    if choice != 'yes':
        continue
    else:
        break
