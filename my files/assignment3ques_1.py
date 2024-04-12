import sqlite3


class PlayerManager:
    def open_menu(self):
        print("Player Manager")
        print("\nview - View Players")
        print("add - Add Players")
        print("del - Delete a Player")
        print("exit - Exit Program")
        command = input("Command: ").lower()
        if command == "view":
            self.view_player()
        elif command == "add":
            self.add_player()
        elif command == "del":
            self.del_player()

    def view_player(self):
        conn = sqlite3.connect('players_manager.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Player")
        players = c.fetchall()
        conn.close()
        print("Players:")
        print(f"Name        Wins     losses     ties      games                    ")
        print(52*"-")
        for player in players:
            player_id, name, wins, losses, ties = player
            print(f"Name: {name}  Wins: {wins}  Losses: {losses}  Ties: {ties}  games: {wins+losses+ties}")

    def add_player(self):
        player_name = input("Enter player name: ")
        player_wins = int(input("Enter player wins: "))
        player_losses = int(input("Enter player losses: "))
        player_ties = int(input("Enter player ties: "))

        conn = sqlite3.connect('players_manager.db')
        c = conn.cursor()
        c.execute("INSERT INTO Player (name, wins, losses, ties) VALUES (?, ?, ?, ?)",
                  (player_name, player_wins, player_losses, player_ties))
        conn.commit()
        conn.close()
        print("Player added successfully.")

    def update_player_stats(self):
        player_id = int(input("Enter the ID of the player to update: "))
        player_wins = int(input("Enter new wins: "))
        player_losses = int(input("Enter new losses: "))
        player_ties = int(input("Enter new ties: "))

        conn = sqlite3.connect('players_manager.db')
        c = conn.cursor()
        c.execute("UPDATE Player SET wins=?, losses=?, ties=? WHERE playerID=?",
                  (player_wins, player_losses, player_ties, player_id))
        conn.commit()
        conn.close()
        print("Player stats updated successfully.")

    def del_player(self):
        player_id = int(input("Enter the ID of the player to delete: "))
        conn = sqlite3.connect('players_manager.db')
        c = conn.cursor()
        c.execute("DELETE FROM Player WHERE playerID = ?", (player_id,))
        conn.commit()
        conn.close()
        print("Player deleted successfully.")

    def create_database(self):
        conn = sqlite3.connect('players_manager.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Player (
                        playerID INTEGER PRIMARY KEY,
                        name TEXT NOT NULL UNIQUE,
                        wins INTEGER NOT NULL,
                        losses INTEGER NOT NULL,
                        ties INTEGER NOT NULL
                     );''')
        conn.commit()
        conn.close()

    def insert_initial_data(self):
        conn = sqlite3.connect('players_manager.db')
        c = conn.cursor()
        initial_data = [
            ('Joel', 3, 7, 10),
            ('Mike', 4, 3, 7)
        ]
        c.executemany("INSERT OR IGNORE INTO Player (name, wins, losses, ties) VALUES (?, ?, ?, ?);", initial_data)
        conn.commit()
        conn.close()


# Create an instance of the PlayerManager class
manager = PlayerManager()
manager.open_menu()
# Create the database table if it doesn't exist
manager.create_database()
# Insert initial player data
manager.insert_initial_data()
