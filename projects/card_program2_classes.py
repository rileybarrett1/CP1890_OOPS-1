import random


class Cards:
    def __init__(self):
        self.suits: str
        self.ranks: str
class Deck:

    def __init__(self):
        self.deck = []
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.__get_deck__()

    def user(self):
        while True:
            num_of_cards = int(input("How many cards would you like: "))
            player_cards = []
            for i in range(num_of_cards):
                player_cards.append(self.deck.pop())
            remander = 52 - num_of_cards
            for card in player_cards:
                print(card)
            if num_of_cards > 52 or num_of_cards < 0:
                print("Pick a number between 1 and 52")
                continue
            print(f"You have {remander} cards left in the deck")
            print("bye!")
            break



    def greeting(self) -> str:
        print("Card Dealer".center(50, "-"))
        print("")

    def shuffle_cards(self):
        random.shuffle(self.deck)


    def __get_deck__(self):
        for suit in self.suits:
            for rank in self.ranks:
                card = f"{rank} of {suit}"
                self.deck.append(card)


    def __str__(self) -> str:
         return str(self.deck)
