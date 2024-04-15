import question_2_bus as bus


def main():
    print("Players Manager\n")
    print("COMMAND MENU\n"
          "view - View players\n"
          "add  - Add a player\n"
          "update - Update a player\n"
          "del  - Delete a player\n"
          "exit - Exit program")

    while True:
        command = input("\nCommand: ")
        if command == "view":
            bus.view_players()
        elif command == "add":
            bus.add_player()
        elif command == "update":
            bus.update_player()
        elif command == "del":
            bus.del_player()
        elif command == "exit":
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
