# Question #2 - Database Tier
import sqlite3


conn = sqlite3.connect("SupportingFiles/Question2/player_db.sqlite")
c = conn.cursor()


def select() -> list:
    return list(c.execute("""SELECT * FROM Player ORDER BY wins DESC;"""))


def insert(name: str, wins: int, losses: int, ties: int) -> None:
    c.execute(f"""INSERT INTO Player VALUES (NULL, "{name}", {wins}, {losses}, {ties});""")
    conn.commit()


def update(name: str, wins: int, losses: int, ties: int) -> None:
    c.execute(f"""UPDATE Player SET wins = {wins}, losses = {losses}, ties = {ties} WHERE name = "{name}";""")
    conn.commit()


def delete(name: str) -> None:
    c.execute(f"""DELETE FROM Player WHERE name = "{name}";""")
    conn.commit()


def main() -> None:
    print(select())
    insert("test", 9, 9, 9)
    print(select())
    update("test", 6, 6, 6)
    print(select())
    delete("test")
    print(select())


if __name__ == "__main__":
    main()
