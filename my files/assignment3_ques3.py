import sqlite3


class TaskManager:
    def open_menu(self):
        while True:
            print("\nTask Manager")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Update Task Status")
            print("4. Delete Task")
            print("5. Complete Task")
            print("6. Exit Program")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.update_task_status()
            elif choice == "4":
                self.del_task()
            elif choice == "5":
                self.complete_task()
            elif choice == "6":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please choose again.")

    def view_tasks(self):
        conn = sqlite3.connect('tasks_manager.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Task")
        tasks = c.fetchall()
        conn.close()
        print("Tasks:")
        print(f"ID  Task Name          Status")
        print("-" * 35)
        for task in tasks:
            task_id, name, status = task
            print(f"{task_id:<3}{name:<20}{status}")

    def add_task(self):
        task_name = input("Enter task name: ")
        status = "Pending"

        conn = sqlite3.connect('tasks_manager.db')
        c = conn.cursor()
        c.execute("INSERT INTO Task (name, status) VALUES (?, ?)",
                  (task_name, status))
        conn.commit()
        conn.close()
        print("Task added successfully.")

    def update_task_status(self):
        task_id = int(input("Enter the ID of the task to update: "))
        new_status = input("Enter new status (Pending/Completed): ").capitalize()

        if new_status not in ['Pending', 'Completed']:
            print("Invalid status. Please enter 'Pending' or 'Completed'.")
            return

        conn = sqlite3.connect('tasks_manager.db')
        c = conn.cursor()
        c.execute("UPDATE Task SET status=? WHERE taskID=?",
                  (new_status, task_id))
        conn.commit()
        conn.close()
        print("Task status updated successfully.")

    def del_task(self):
        task_id = int(input("Enter the ID of the task to delete: "))
        conn = sqlite3.connect('tasks_manager.db')
        c = conn.cursor()
        c.execute("DELETE FROM Task WHERE taskID = ?", (task_id,))
        conn.commit()
        conn.close()
        print("Task deleted successfully.")

    def complete_task(self):
        task_id = int(input("Enter the ID of the task to mark as completed: "))
        conn = sqlite3.connect('tasks_manager.db')
        c = conn.cursor()
        

