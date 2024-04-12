from card_dealer import Card, Deck


def main():
    print("Card Dealer".center(50, "-"))
    print("")
    while True:
        my_deck.shuffle()
        num_of_cards = int(input("\nhow many cards would you like:"))
        if num_of_cards > 52 or num_of_cards <= 0:
            print("Please enter a number less than the deck 52 or greater then zero")
            continue
        else:

            print()
            player_cards = []

            for i in range(num_of_cards):
                player_cards.append(my_cards)
            for card in player_cards:
                print(card)
            amount = 52 - num_of_cards
            print(f"\nYou have {amount} cards left in the deck! ")

            print("goodbye!")
            break
            




my_cards = Card()
my_deck = Deck()

if __name__ == '__main__':
    main()
