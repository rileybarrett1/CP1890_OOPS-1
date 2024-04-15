import question_3_bus as bus


def main():
    print("Task List\n")
    print("COMMAND MENU")
    print("view     - View pending tasks\n"
          "history  - View completed tasks\n"
          "add      - Add a task\n"
          "complete - Complete a task\n"
          "delete   - Delete a task\n"
          "exit     - Exit program")

    while True:
        command = input("\nCommand: ")
        if command == 'view':
            bus.view_task()
        elif command == 'history':
            bus.view_hist()
        elif command == 'add':
            bus.add_task()
        elif command == 'complete':
            bus.comp_task()
        elif command == "delete":
            bus.del_task()
        elif command == "exit":
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
