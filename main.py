import platform
import os

define = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

def cardgen():
    import random
    
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    face = ['J', 'Q', 'K', 'A']
    
    deck = (number+face)*4
    random.shuffle(deck)
    return deck

def start():
    import copy

    print("\n\n__________________________________")
    print("\nGame has begun...")

    start_hand(player)
    start_hand(dealer)
    check(player)
    check(dealer)
    show_hand(player)

    hand = copy.deepcopy(dealer.cards)
    hand[1] = '_'
    hand = str(hand).strip("[]").replace("'","")
    print(f"\nDealer's hand: {hand}")
    print("Total: ?")

    print(f"\nBank Total: {player.bank}")
    print(f"\nBetted Amount: {bet_amount}")

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
            print(f"\nBank Total: {player.bank}")
            print(f"\nBetted Amount: {bet_amount}")

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
        return "BUST"
    else:
        if total_sum(dealer) == total_sum(player):
            return "TIE"

        elif total_sum(dealer) > 21:
            player.add_bank(bet_amount)
            return player
            
        elif total_sum(player) > 21:
            player.lose_bank(bet_amount)
            return dealer

        elif total_sum(dealer) > total_sum(player):
            player.lose_bank(bet_amount)
            return dealer
        
        elif total_sum(player) > total_sum(dealer):
            player.add_bank(bet_amount)
            return player

def finish(user):
    print("\n\n__________________________________")
    if user == "TIE":
        print("\nIT IS A TIE")
        show_hand(player)
        show_hand(dealer)
    elif user == "BUST":
        print("\nBOTH HAS BUSTED")
        show_hand(player)
        show_hand(dealer)
    else:
        print(f"\n{user.name.upper()} HAS WON!!")
        show_hand(user)

def bet(user):
    print("\n\n__________________________________")
    print(f"\nBank Total: {player.bank}")
    while True:
        try:
            amount = int(input("\nEnter your bet...\n"))

            if amount > user.bank:
                print("This is over your bank budget!")   
                print("please choose an appropriate amount corresponding to you bank amount")
            elif amount < 0:
                print("please choose an appropriate amount corresponding to you bank amount")
            elif amount == 0:
                print("Amount must be above zero")
            else:
                return amount            
        except:
            print("Please enter an interger number (E.G 0 1 2 3 50 ...)")

def check_amount():
    if player.bank <= 0:
        print("\nYOU HAVE NO MORE DOSH!!")
        print(f"\nBank Total: {player.bank}")
        while True:
            restart = input("\nRESTART?     (yes/no)\n")
            if restart.lower() == 'yes':
                player.bank = 1000
                operating_system()
                player.cards = []
                dealer.cards = []
                return "RESTART"
            elif restart.lower() == 'no':
                operating_system()
                return "EXIT"
            else:
                print("Please choose either 'Yes' or 'No'")

def check(user):
    if 'A' in user.cards and total_sum(user) > 21:
        user.define_hand['A'] = 1
    if total_sum(user) > 21:
        return True
    else:
        return False

def total_sum(user):
    total = 0
    for i in user.cards:
        total += user.define_hand[i]
    return total

def start_hand(user):
    for i in range(2):
        # user.cards.append(deck[i])
        user.cards.append('A')
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
    import copy
    define_hand = copy.deepcopy(define)
    def __init__(self, name, bank, cards=[]):
        self.cards = cards
        self.name = name
        self.bank = bank

    def lose_bank(self, bet):
        self.bank -= bet

    def add_bank(self, bet):
        self.bank += bet

class Dealer():
    import copy
    define_hand = copy.deepcopy(define)
    def __init__(self, name="Dealer", cards=[]):
        self.cards = cards
        self.name = name

def replay():
    while True:
        replay = input("\n\nContinue?     (Yes/No)\n")
        if replay.lower() == 'yes' or replay.lower() == 'y':
            operating_system()
            player.cards = []
            dealer.cards = []
            break
        elif replay.lower() == 'no' or replay.lower() == 'n':
            operating_system()
            return True
        else:
            print("Please choose either 'Yes' or 'No'")

# Game Start

print("Welcome to Blackjack")
print("\nThe goal of the game is to get as close to 21 as possible and have the total higher then the dealer!\n")
name = input("\nPlease enter your name...\n")

deck = cardgen()
player = Player(name, 1000, [])
dealer = Dealer("Dealer", [])

while True:
    
    bet_amount = bet(player)
    start()
    choice(player)
    ai()
    finish(winner())
    again = check_amount()
    if again == "RESTART":
        continue
    elif again == "EXIT":
        break
    if replay():
        break
