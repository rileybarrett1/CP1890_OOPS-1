# Question #3 - Business Tier
import Question3_Database as Db


def get_int(prompt: str) -> int:
    while True:
        response = input(prompt)
        if response.isnumeric():
            response = int(response)
            if 1 <= response <= len(Db.history()):
                return response
        print("Invalid input. Please try again.\n")


def view() -> None:
    for n, t in enumerate(Db.view(), 1):
        print(f"{n}. {t[1]}")


def history() -> None:
    for n, t in enumerate(Db.history(), 1):
        print(f"{n}. {t[1]} (DONE!)")


def add() -> None:
    desc = input("Description: ").capitalize()
    Db.add(desc)


def complete() -> None:
    index = get_int("Number: ")
    Db.complete(Db.view()[index - 1][1])


def delete() -> None:
    index = get_int("Number: ")
    Db.delete(Db.history()[index - 1][1])


def main() -> None:
    view()
    history()


if __name__ == "__main__":
    main()
