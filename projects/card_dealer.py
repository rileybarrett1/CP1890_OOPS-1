import random


class Card:


    def __init__(self):
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

    def get_suit(self):
        return random.choice(self.suits)

    def get_rank(self):
        return random.choice(self.ranks)

    def __str__(self):
        return f'{self.get_rank()} of {self.get_suit()}'

    def set_rank(self, rank):
        pass

    def __repr__(self) -> str:
        return str(f"{self.ranks} of {self.suits}")





class Deck:
    def __init__(self):
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        self.cards = []

    def populate_deck(self, suits, ranks):
        for suit in suits:
            for rank in ranks:
                self.cards.append(f"{rank} of {suit}")

    def count_cards(self):
        return len(f"there are {self.cards} left in the deck")

    def shuffle(self):
        print("I have shuffled a deck of 52 cards")
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            return "no more cards left in the deck"
        else:
            return self.cards.pop()

