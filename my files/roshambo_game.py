from dataclasses import dataclass
from random import random

from sqlalchemy.sql.functions import user


class RoshamboGame:
    @dataclass
    def __init__(self):
        score: 0
        rock: str = "r"
        paper: str = "p"
        scissors: str = "s"

    def rock_paper_scissors(self):
        user = input("rock, paper, or scissors(r/p/s)")
        if user == "r":
            return "rock"
        if user == "p":
            return "paper"
        if user == "s":
            return "scissors"
        else:
            print("Invalid selection r, p or s")

        # def players(self):
        #     players = ["Joel", "Hart", "Bart"]
        #     return players


class Player:
    name: str = "<NAME>"
    roshambo: str
    __wins: int = 0
    __losses: int = 0

    def computer(self):
        computer = ["Joel", "Hart", "Bart"]
        for j in range(0, 3):
            return computer[random.randint(0, 3)]
        for h in range(0, 3):
            return computer[random.randint(0, 3)]
        for b in range(0, 3):
            return computer[random.randint(0, 3)]
        if computer[0]:
            return "Rock"
        if computer[1]:
            return "Paper"
        if computer[2]:
            return "Scissors"

    def play(self, other_player):
        if self.roshambo == other_player.roshambo:
            return None
        else:
            if (self.roshambo == "rock" and other_player.roshambo == "scissors") \
                    or (self.roshambo == "paper" and other_player == "rock") \
                    or (self.roshambo == "scissors" and other_player == "paper"):
                return self
            else
                return other_player

    @property
    def wins(self):
        return self.__wins

    @property
    def losses(self):
        return self.__losses

    def add_win(self, other_player):
        self.__wins += 1

    def add_loss(self, other_player):
        self.__losses += 1

    def __str__(self):
        return f"{self.name}{self.roshambo}"


@dataclass
class bart(Player):

    def __post_init__(self):
        self.name = "bart"


@dataclass
class hart(Player):
    def __post_init__(self):
        self.name = "Hart"

    def generateroshambo(self):
        self.roshambo = random.choice(self.user)


@dataclass
class Joel(Player):
    def __post_init__(self):
        self.name = "Joel"

    def generateroshambo(self):
        self.roshambo = random.choice(self.user)


def main():
    print("roshambo game")
    name = input("enter your name ")

    player1 = Player(name)
    opponent = input("would you like to play against hart or bart or joel")
    print()

    if opponent == "b":
        player1 = bart()
    if player1 == "h":
        player1 = hart()
    if player1 == "joel":
        player1 = Joel()

    play_again = "y"
    while play_again.lower() == "y":
        selection = input("rock,paper,or,scissors")
        if selection == "paper":
            player1.roshambo = 'Paper'
        if selection == "rock":
            player1.roshambo = "rock"
        if selection == "scissors":
            player1.roshambo = "Scissors"

        else:
            print("invalid selection")
            continue

        player2.generateroshambo()

        print(player1)
        print(player2)

        winner = player1.play(player2)
        if winner is None:
            print('draw\n')
        else:
            print(f"{winner.name} wins!\n")
            winner.add_win()
            if winner is player1:
                player2.add_loss()
            else:
                player1.add_loss()
