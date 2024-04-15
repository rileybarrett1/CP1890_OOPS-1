# Question #2 - Business Tier
import Question2_Database as Db


def get_int(prompt: str) -> int:
    while True:
        response = input(prompt)
        if response.isnumeric():
            response = int(response)
            if response >= 0:
                return response
        print("Invalid input. Please try again.\n")


def view() -> None:
    print(f"{'Name':12}{'Wins':>8}{'Losses':>10}{'Ties':>10}{'Games':>10}")
    print(50 * '-')
    for player in Db.select():
        print(f"{player[1]:12}{player[2]:>8}{player[3]:>10}{player[4]:>10}{sum(player[2:4]):>10}")


def add() -> None:
    name = input("Name: ").title()
    wins = get_int("Wins: ")
    losses = get_int("Losses: ")
    ties = get_int("Ties: ")

    Db.insert(name, wins, losses, ties)
    print(f"{name} was added to database.")


def update() -> None:
    name = input("Name: ").title()
    wins = get_int("Wins: ")
    losses = get_int("Losses: ")
    ties = get_int("Ties: ")

    Db.update(name, wins, losses, ties)
    print(f"{name} was updated.")


def delete() -> None:
    name = input("Name: ").title()
    Db.delete(name)
    print(f"{name} was deleted from database.")


def main() -> None:
    view()
    add()
    view()
    delete()
    view()


if __name__ == "__main__":
    main()
