import time
import random

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("Welcome to the Mysterious Adventure Game!")
    slow_print("You find yourself in a dark room.")
    slow_print("You can see three doors in front of you.")

def choose_door():
    slow_print("Which door do you choose? (1, 2, or 3)")
    choice = input("> ")
    if choice in ['1', '2', '3']:
        return int(choice)
    else:
        slow_print("Invalid choice! Please choose again.")
        return choose_door()

def enter_room(room_number):
    slow_print(f"You open door {room_number} and enter the room...")
    time.sleep(1)
    # Generate a random challenge
    challenge = random.choice(challenges)
    slow_print(challenge["description"])
    if challenge["type"] == "quiz":
        solve_quiz(challenge)
    elif challenge["type"] == "riddle":
        solve_riddle(challenge)
    elif challenge["type"] == "combat":
        fight_enemy(challenge)
    slow_print("You continue your adventure...")

def solve_quiz(challenge):
    slow_print("You encounter a quiz challenge!")
    slow_print("Answer the following question:")
    slow_print(f"Question: {challenge['question']}")
    slow_print("Options:")
    for i, option in enumerate(challenge['options'], 1):
        slow_print(f"{i}. {option}")
    answer = input("Your answer (1, 2, 3, or 4): ")
    if answer == str(challenge['answer']):
        slow_print("Congratulations! You answered correctly.")
    else:
        slow_print("Sorry, that's incorrect. Better luck next time.")

def solve_riddle(challenge):
    slow_print("You encounter a riddle challenge!")
    slow_print("Here's the riddle:")
    slow_print(challenge['riddle'])
    answer = input("Your answer: ").strip().lower()
    if answer == challenge['answer'].lower():
        slow_print("Well done! You solved the riddle.")
    else:
        slow_print("That's not correct. The correct answer was:", 0.05)
        slow_print(challenge['answer'], 0.05)

def fight_enemy(challenge):
    slow_print("You encounter an enemy!")
    slow_print(f"You're facing a {challenge['enemy']}!")
    while challenge['health'] > 0:
        slow_print(f"The {challenge['enemy']} has {challenge['health']} health.")
        attack = input("Do you want to attack? (yes/no): ").lower()
        if attack == 'yes':
            damage = random.randint(10, 30)
            challenge['health'] -= damage
            slow_print(f"You attack the {challenge['enemy']} and deal {damage} damage!")
        else:
            slow_print("You decide not to attack.")
            slow_print("The enemy attacks you!")
            your_health = random.randint(20, 50)
            slow_print(f"You lose {your_health} health!")
            break
    if challenge['health'] <= 0:
        slow_print(f"You defeated the {challenge['enemy']}!")
    else:
        slow_print("Game Over! You were defeated by the enemy.")

def play_game():
    intro()
    inventory = []
    for i in range(1, 6):  # Loop for five rooms
        room_number = choose_door()
        item = enter_room(room_number, inventory)
        if item:
            inventory.append(item)
    slow_print("Congratulations! You've completed the adventure.")

def enter_room(room_number, inventory):
    slow_print(f"You open door {room_number} and enter the room...")
    time.sleep(1)
    # Generate a random challenge
    challenge = random.choice(challenges)
    slow_print(challenge["description"])
    if challenge["type"] == "quiz":
        solve_quiz(challenge)
    elif challenge["type"] == "riddle":
        solve_riddle(challenge)
    elif challenge["type"] == "combat":
        fight_enemy(challenge)
    elif challenge["type"] == "treasure":
        collect_treasure(challenge, inventory)
    slow_print("You continue your adventure...")

def collect_treasure(challenge, inventory):
    slow_print("You find a treasure chest!")
    item = challenge['item']
    slow_print(f"You found a {item}!")
    choice = input("Do you want to take it? (yes/no): ").lower()
    if choice == 'yes':
        slow_print(f"You add the {item} to your inventory.")
        return item
    else:
        slow_print("You decide not to take the item.")
        return None

challenges = [
    {"type": "quiz", "description": "You encounter a locked chest. To open it, you must solve a quiz.", "question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Rome"], "answer": 2},
    {"type": "riddle", "description": "You see a mysterious inscription on the wall. It seems to be a riddle.", "riddle": "What has keys but can't open locks?", "answer": "keyboard"},
    {"type": "combat", "description": "A fierce monster blocks your path!", "enemy": "goblin", "health": 100},
    {"type": "combat", "description": "You encounter a fearsome dragon!", "enemy": "dragon", "health": 150},
    {"type": "treasure", "description": "You stumble upon a hidden treasure chest.", "item": "golden key"}
]
if __name__ == "__main__":
    play_game()