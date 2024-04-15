# Question #2 - Presentation Tier
import Question2_Business as Bis


def main() -> None:
    print("Player Manager\n"
          "\n"
          "COMMAND MENU\n"
          "view   - View players\n"
          "add    - Add a player\n"
          "update - Update a player\n"
          "del    - Delete a player\n"
          "exit   - Exit program")

    while True:
        command = input("\nCommand: ").lower()

        if command == 'view':
            Bis.view()
        elif command == 'add':
            Bis.add()
        elif command == 'update':
            Bis.update()
        elif command == 'del':
            Bis.delete()
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
