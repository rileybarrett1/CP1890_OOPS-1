from dataclasses import dataclass


@dataclass
class Player:
    player_name: str
    player_position: str
    player_score: int
    player_average_score: float
    player_ab: int
    player_h: int

    def score(self):
        if self.player_score > 0:
            print("must be greater than zero")
        return self.player_score

    def average_score(self):
        if self.player_score > 0:
            print("must be greater then zero")
        else:
            return self.player_average_score

    def players_h(self):
        if self.player_h > 0:
            print("must be greater then zero")
        else:
            return self.player_h

    def average_bat(self):
        if self.player_ab > 0:
            print("must be greater then zero")
        else:
            return self.player_ab
