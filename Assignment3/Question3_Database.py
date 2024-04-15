# Question #3 - Database Tier
import sqlite3


conn = sqlite3.connect("SupportingFiles/Question3/task_list_db.sqlite")
c = conn.cursor()


def view() -> list:
    return list(c.execute("""SELECT * FROM Task WHERE completed = 0;"""))


def history() -> list:
    return list(c.execute("""SELECT * FROM Task WHERE completed = 1;"""))


def add(description: str) -> None:
    c.execute(f"""INSERT INTO Task VALUES (NULL, "{description}", 0);""")
    conn.commit()


def complete(description: str) -> None:
    c.execute(f"""UPDATE Task SET completed = 1 WHERE description = "{description}";""")
    conn.commit()


def delete(description: str) -> None:
    c.execute(f"""DELETE FROM Task WHERE description = "{description}";""")
    conn.commit()


def main() -> None:
    print(view())
    print(history())


if __name__ == "__main__":
    main()
