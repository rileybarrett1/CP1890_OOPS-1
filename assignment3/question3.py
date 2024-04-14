import sqlite3

class TaskManager:
    def __init__(self):
        self.create_database()

    def open_menu(self):
        print("Task Manager")
        print("\nview - View Incomplete Tasks")
        print("add - Add Task")
        print("complete - Mark Task as Completed")
        print("history - View Completed Tasks")
        print("exit - Exit Program")
        command = input("Command: ").lower()
        if command == "view":
            self.view_incomplete_tasks()
        elif command == "add":
            self.add_task()
        elif command == "complete":
            self.complete_task()
        elif command == "history":
            self.view_completed_tasks()
        elif command == "exit":
            print("Exiting program...")
        else:
            print("Invalid command. Please try again.")

    def view_incomplete_tasks(self):
        try:
            conn = sqlite3.connect('task_list.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Task WHERE completed = 0")
            tasks = cursor.fetchall()
            if not tasks:
                print("No incomplete tasks found.")
            else:
                print("Incomplete Tasks:")
                for task in tasks:
                    print(f"ID: {task[0]}, Description: {task[1]}")
        except sqlite3.Error as error:
            print("Error viewing incomplete tasks:", error)
        finally:
            if conn:
                conn.close()

    def add_task(self):
        description = input("Enter task description: ")
        try:
            conn = sqlite3.connect('task_list.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Task (description) VALUES (?)", (description,))
            conn.commit()
            print("Task added successfully.")
        except sqlite3.Error as error:
            print("Error adding task:", error)
        finally:
            if conn:
                conn.close()

    def complete_task(self):
        task_id = input("Enter task ID to mark as completed: ")
        try:
            conn = sqlite3.connect('task_list.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE Task SET completed = 1 WHERE taskID = ?", (task_id,))
            conn.commit()
            print("Task marked as completed.")
        except sqlite3.Error as error:
            print("Error completing task:", error)
        finally:
            if conn:
                conn.close()

    def view_completed_tasks(self):
        try:
            conn = sqlite3.connect('task_list.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Task WHERE completed = 1")
            tasks = cursor.fetchall()
            if not tasks:
                print("No completed tasks found.")
            else:
                print("Completed Tasks:")
                for task in tasks:
                    print(f"ID: {task[0]}, Description: {task[1]}")
        except sqlite3.Error as error:
            print("Error viewing completed tasks:", error)
        finally:
            if conn:
                conn.close()

    def create_database(self):
        try:
            conn = sqlite3.connect('task_list.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Task (
                                taskID INTEGER PRIMARY KEY,
                                description TEXT NOT NULL,
                                completed INTEGER NOT NULL DEFAULT 0
                            );''')
            conn.commit()
            print("Task database created successfully!")
        except sqlite3.Error as error:
            print("Error creating task database:", error)
        finally:
            if conn:
                conn.close()

if __name__ == '__main__':

    manager = TaskManager()
    manager.open_menu()
