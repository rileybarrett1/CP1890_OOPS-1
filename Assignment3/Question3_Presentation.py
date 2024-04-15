# Question #3 - Presentation Tier
import Question3_Business as Bis


def main() -> None:
    print("Task List\n"
          "\n"
          "COMMAND MENU\n"
          "view     - View pending tasks\n"
          "history  - View completed tasks\n"
          "add      - Add a task\n"
          "complete - Complete a task\n"
          "delete   - Delete a task\n"
          "exit     - Exit program")

    while True:
        command = input("\nCommand: ").lower()

        if command == 'view':
            Bis.view()
        elif command == 'history':
            Bis.history()
        elif command == 'add':
            Bis.add()
        elif command == 'complete':
            Bis.complete()
        elif command == 'delete':
            Bis.delete()
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
