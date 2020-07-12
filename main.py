import platform
import os

def cardgen():
    import random
    
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    face = ['J', 'Q', 'K', 'A']
    
    deck = (number+face)*4
    random.shuffle(deck)
    return deck

def start():
    import copy

    print("\n\nGame has begun...")

    start_hand(player)
    start_hand(dealer)
    show_players_hand()

    hand = copy.deepcopy(dealer.cards)
    hand[1] = '_'
    hand = str(hand).strip("[]").replace("'","")
    print(f"\nDealer's hand: {hand}")
    print("Total: ?")

def show_players_hand():
    hand = str(player.cards).strip("[]").replace("'","")
    print(f"\n{player.name}'s hand: {hand}")
    print(f"Total: {total_sum(player)}")

def choice(user):
    while True:
        print("\n\n__________________________________")
        decision = str(input("\nHIT or STAY\n"))
        if decision.lower() == 'hit':
            add_card(player)
            show_players_hand()
        elif decision.lower() == 'stay':
            break
        else:
            print("Please input either 'HIT' or 'STAY'")
        
        if check(user) == True:
            break
    
def check(user):
    if total_sum(user) > 21:
        print(f"{user.name.upper()} HAVE BUSTED")
        return True

def total_sum(user):
    total = 0
    for i in user.cards:
        total += define[i]
    return total

def start_hand(user):
    for i in range(2):
        user.cards.append(deck[i])
    del deck[:2]
        
def add_card(user):
    user.cards.append(deck[0])
    deck.pop(0)

class Player():
    def __init__(self, name, cards=[]):
        self.cards = cards
        self.name = name

class Dealer():
    def __init__(self, cards=[]):
        self.cards = cards

define = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
deck = cardgen()

def replay():
    while True:
        replay = input("\n\nReplay?     (Yes/No)\n")
        if replay.lower() == 'yes' or replay.lower() == 'y':
            break
        elif replay.lower() == 'no' or replay.lower() == 'n':
            op = platform.system()
            if op == 'Darwin':
                os.system('clear')
            elif op == 'Windows':
                os.system('cls')
            elif op == 'Linux':
                os.system('clear')
            else:
                os.system('clear')
            return True
        else:
            print("Please choose either 'Yes' or 'No'")

# Game Start

while True:
    print("\n\n\nWelcome to Blackjack")
    print("\nThe goal of the game is to get as close to 21 as possible and have the total higher then the dealer!\n")
    name = input("\nPlease enter your name...\n")
    player = Player(name)
    dealer = Dealer()
    start()
    choice(player)
    if replay():
        break
