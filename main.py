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
    show_hand(player)

    hand = copy.deepcopy(dealer.cards)
    hand[1] = '_'
    hand = str(hand).strip("[]").replace("'","")
    print(f"\nDealer's hand: {hand}")
    print("Total: ?")

def show_hand(user):
    hand = str(user.cards).strip("[]").replace("'","")
    print(f"\n{user.name}'s hand: {hand}")
    print(f"Total: {total_sum(user)}")

def choice(user):
    while True:
        print("\n\n__________________________________")
        decision = str(input("\nHIT or STAY\n"))
        if decision.lower() == 'hit':
            add_card(user)
            show_hand(user)
        elif decision.lower() == 'stay':
            break
        else:
            print("Please input either 'HIT' or 'STAY'")
        
        if check(user) == True:
            print(f"{user.name.upper()} HAS BUSTED")
            break

def ai():
    while True:
        if total_sum(dealer) < 17:
            add_card(dealer)
        elif total_sum(dealer) > 16:
            break
        if check(dealer) == True:
            show_hand(dealer)
            print("DEALER HAS BUSTED")
            break

def winner():
    if check(dealer) == True and check(player) == True:
        return "TIE"
    else:
        if total_sum(dealer) == total_sum(player):
            return "TIE"

        if total_sum(dealer) > 21:
            return player
            
        elif total_sum(player) > 21:
            return dealer

        if total_sum(dealer) > total_sum(player):
            return dealer
        
        elif total_sum(player) > total_sum(dealer):
            return player

def finish(user):
    print("\n\n__________________________________")
    if user == "TIE":
        print("\nIT IS A TIE")
    else:
        print(f"\n{user.name.upper()} HAS WON!!")
        show_hand(user)
    
def check(user):
    if total_sum(user) > 21:
        return True
    else:
        return False

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

def operating_system():
    op = platform.system()
    if op == 'Darwin':
        os.system('clear')
    elif op == 'Windows':
        os.system('cls')
    elif op == 'Linux':
        os.system('clear')
    else:
        os.system('clear')

class Player():
    def __init__(self, name, cards=[]):
        self.cards = cards
        self.name = name

class Dealer():
    def __init__(self, name="Dealer", cards=[]):
        self.cards = cards
        self.name = name

def replay():
    while True:
        replay = input("\n\nReplay?     (Yes/No)\n")
        if replay.lower() == 'yes' or replay.lower() == 'y':
            operating_system()
            break
        elif replay.lower() == 'no' or replay.lower() == 'n':
            operating_system()
            return True
        else:
            print("Please choose either 'Yes' or 'No'")

define = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

# Game Start


while True:
    print("Welcome to Blackjack")
    print("\nThe goal of the game is to get as close to 21 as possible and have the total higher then the dealer!\n")
    name = input("\nPlease enter your name...\n")
    deck = cardgen()
    player = Player(name, [])
    dealer = Dealer("Dealer", [])
    start()
    choice(player)
    ai()
    finish(winner())
    if replay():
        break
