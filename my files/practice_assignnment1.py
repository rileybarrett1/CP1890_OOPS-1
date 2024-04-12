import random


class List(list):
    def __init__(self):
        self.random_list = []


class randomint_list(list):
    def __init__(self, n):

        if not (0 < n <= 100):
            raise ValueError("Please enter an integer between 1 and 100")
        super().__init__(random.randint(0, 100) for _ in range(n))

    def total(self):
        return sum(self)

    def __str__(self):
        return str(", ".join(map(str, self)))

    def average(self):
        return sum(self) / len(self)



while True:
    print("\nrandom integer list")
    print("")
    n = int(input("How many random integers should the list contain: ").lower())
    if 0 < n <= 100:
        random_list = randomint_list(n)
        print("Random Integers")
        print(10 * "=")
        print(f"integers: {random_list}")
        print(f"Count: {len(random_list)}")
        print(f"Total: {random_list.total():.2f}")
        print(f"Average: {random_list.average():.2f}")
        print("")
        cont = input("Continue? (y/n): ")
        if cont != "n":
            continue
        else:
            break