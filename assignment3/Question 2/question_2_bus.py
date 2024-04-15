import question_2_db as db


def get_number(num):
    while True:
        number = input(num)
        if number.isnumeric():
            num_int = int(number)
            if num_int >= 0:
                return number


def view_players():
    print(f"{'Name':16} {'Wins':>8} {'Losses':>11} {'ties':>8} {'Games':>10}")
    print("-"*57)
    for player in db.select_all():
        print(f"{player[1]:16} {player[2]:>8} {player[3]:11} {player[4]:>8}{sum(player[2:4]):>10}")


def add_player():
    p_name = input("Name: ")
    p_wins = input("Wins: ")
    p_losses = input("Losses: ")
    p_ties = input("Ties: ")
    db.add_player(p_name, p_wins, p_losses, p_ties)
    print(f"{p_name} was added to the database")


def del_player():
    player_name = input("Name: ")
    db.delete_player(player_name)
    print(f"{player_name} was deleted from the database")


def update_player():
    p_name = input("Name: ")
    p_wins = input("Wins: ")
    p_losses = input("Losses: ")
    p_ties = input("Ties: ")
    db.update_player(p_name, p_wins, p_losses, p_ties)
    print(f"{p_name} was updated in the database")
