class Players:
    player = str
    pos = str
    ab = int
    hits = int
    avg = float

class Lineup(Players):
    def the_lineup(self):
        player_lineup = [["tommy la stella", "3b", 1316, 360, 0.274],
                         ["mike yastrzmski", "rf", 563, 168, 0.281],
                         ["donavan solano", "2b", 1473, 407, 0.276],
                         ["Buster posey", "c", 5473, 1380, 0.302],
                         ["Brandon belt", "1b", 3811, 1003, 0.263],
                         ["Brandon crawford", "ss", 4402, 1099, 0.250],
                         ["alex dickerson", "Lf", 586, 160, 0.273],
                         ["austin slater", "CF", 569, 147, 0.274],
                         ["kein gausman", "P", 56, 2, 0.036]]
        positions = ["c", "1b", "2b", "3b", "ss", "lf", "cf", "rf", "f"]

        def add_player(self):
            self.player = 0
            self.pos = positions[self.player]
            self.player = (self.player + 1)
            self.hits = 0
            self.avg = float(self)
            return self.player
            # player_lineup.append(player_name, pos, player_average_bat, player_hits, player_hits)

        def drop_player(self, player_name):
            if player_name == "":
                self.player = 0
                self.pos = positions[self.player]
                self.player = (self.player + 1)
                self.hits = 0
                self.avg = float(self)
                return self.player
            # drop_player = input("enter player number :")
            # player_lineup.remove(drop_player)
