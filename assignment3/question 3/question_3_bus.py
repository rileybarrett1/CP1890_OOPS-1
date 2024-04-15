import question_3_db as db

# system function for tasks


def get_number(num):
    while True:
        number = input(num)
        if number.isnumeric():
            num_int = int(number)
            if 0 <= num_int <= len(db.view_hist()):
                return num_int
        else:
            print("invalid input")


def view_task():
    for i, t in enumerate(db.view_tasks(), 1):
        print(f"{i}. {t[1]}")


def view_hist():
    for i, t in enumerate(db.view_hist(), 1):
        print(f"{i}. {t[1]} (Done!)")


def add_task():
    description = input("Description: ")
    db.add_task(description)


def comp_task():
    num = get_number("Number: ")
    db.comp_task(db.view_tasks()[num - 1][1])


def del_task():
    num = get_number("Number: ")
    db.del_task(db.view_hist()[num - 1][1])
